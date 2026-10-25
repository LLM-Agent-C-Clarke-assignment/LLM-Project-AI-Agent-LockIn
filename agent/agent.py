

from tools.nutrition_tool import calculate_nutrition
from tools.recipe_tool import recipe_tool
from tools.budget_tool import manage_grocery_budget
from tools.storage_tool import save_meal_plan

from database import create_table, save_plan
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, END


import json
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOllama(
    model="llama3.2",
    temperature=0.3,
    num_predict=512,
    keep_alive="5m"

)


def generate_meal_plan(user_request):
    """Generate a meal plan from the Streamlit UI inputs."""

    prompt = f"""
Create a personalized meal plan using these user requirements.

{json.dumps(user_request, indent=2, ensure_ascii=False)}

Requirements:
- Follow the fitness goal and meal plan duration.
- Respect all allergies and dietary restrictions.
- Use food preferences where suitable.
- Consider the grocery budget in LKR.
- Use pantry ingredients when suitable.
- Provide ingredients, quantities, preparation steps,
  estimated grocery costs and a shopping list.
- Clearly label costs as estimates, not verified prices.
- Do not invent tool results or claim that tools were executed.
- If reliable ingredient prices are unavailable, say so.
- Never recommend a known allergen.
- Organize the plan by day and meal.

Return a clear, readable meal plan.
"""

    
def generate_meal_plan(user_request):
    prompt = f"""
Create a personalized meal plan using these requirements:

{json.dumps(user_request, indent=2, ensure_ascii=False)}

Generate the recipe step by step.
Include ingredients, quantities, cooking instructions,
estimated costs, and a shopping list.
Respect all allergies and dietary restrictions.
"""

    messages = [
        SystemMessage(
            content="You are NutriChef AI, a helpful meal planning assistant."
        ),
        HumanMessage(content=prompt)
    ]

    full_response = ""

    for chunk in llm.stream(messages):
        if chunk.content:
            full_response += chunk.content

    return full_response



SYSTEM_PROMPT = """
You are NutriChef AI, an intelligent recipe and grocery planning assistant.

YOUR ROLE:
Help users create personalized meal plans based on their fitness goals,
food preferences, allergies, dietary restrictions, grocery budget, and
available pantry ingredients.

SUPPORTED FITNESS GOALS:
- Weight Loss
- Weight Gain
- Muscle Gain
- Healthy Eating

AVAILABLE TOOLS:
1. get_food_suggestions()
   Find suitable recipes based on fitness goals, food preferences,
   allergies, and dietary restrictions.

2. manage_grocery_budget()
   Estimate ingredient costs and check whether a meal plan fits
   the user's grocery budget.

3. calculate_nutrition()
   Estimate the nutritional values of selected ingredients and meals.

4. save_meal_plan()
   Save the final meal plan for future access.

RULES:
1. Understand the user's fitness goal and dietary requirements before
   recommending recipes.
2. Use the recipe tool to obtain recipes from the available dataset.
3. Never intentionally recommend recipes containing ingredients
   identified as allergens by the user.
4. Respect the user's dietary restrictions and food preferences.
5. Use the budget tool to estimate grocery costs.
6. If the estimated cost exceeds the budget, try suitable ingredient
   substitutions or select more affordable recipes, then recalculate
   the cost.
7. Do not invent ingredient prices, recipes, tool results, or nutrition
   values.
8. Use the nutrition tool when nutritional estimates are requested or
   required by the task.
9. Save the final meal plan only when requested by the user or when
   required by the application workflow.
10. If a required detail is missing, ask the user a relevant question.
11. Clearly explain the meal plan, estimated cost, substitutions,
    shopping list, and pantry items when this information is available.
12. Distinguish estimated costs and nutrition values from verified data.
13. Never claim that a tool succeeded unless its result confirms success.
14. Do not provide medical diagnoses or claim that a meal plan treats
    a medical condition.

RESPONSE FORMAT:
- Fitness goal
- Recommended meal plan
- Ingredients and quantities
- Estimated grocery cost
- Budget status
- Suggested substitutions, if needed
- Shopping list
- Ingredients already available in the pantry
- Nutrition estimates, when available

IMPORTANT:
Use the available tools for calculations and data retrieval.
Do not pretend to have executed a tool when you have not.
Be friendly, accurate, and concise.
"""




def run_agent(ingredients, budget, allergies=None,
              dietary_restrictions=None):

    create_table()

    recipe = recipe_tool(
        ingredients,
        allergies=allergies,
        dietary_restrictions=dietary_restrictions
    )

    if recipe.get("error") or not recipe.get("recipe_generated"):
        return recipe

   
    nutrition = calculate_nutrition(ingredients)

    if "error" in nutrition:
        return nutrition

 
    grocery = [
        {
            "name": item["name"],
            "quantity": float(item["quantity"]) / 1000
        }
        for item in ingredients
    ]

    budget_result = manage_grocery_budget(grocery, budget)

    if "error" in budget_result:
        return budget_result

    if not budget_result["within_budget"]:
        return {
            "error": "Meal exceeds your budget.",
            "budget": budget_result
        }

    
    plan = {
        "recipe": recipe,
        "nutrition": nutrition,
        "budget": budget_result
    }

    storage = save_meal_plan(plan)

    if "error" in storage:
        return storage

    database = save_plan(plan)

    if "error" in database:
        return database

    return {
        "success": True,
        "meal_plan": plan,
        "saved_file": storage["file_name"]
    }
