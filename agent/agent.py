
from agent.tools.nutrition_tool import calculate_nutrition
from agent.tools.recipe_tool import recipe_tool
from agent.tools.budget_tool import manage_grocery_budget
from agent.tools.storage_tool import save_meal_plan

from agent.database import create_table, save_plan


def run_agent(ingredients, budget, allergies=None,
              dietary_restrictions=None):

    create_table()

    # Check recipe suitability
    recipe = recipe_tool(
        ingredients,
        allergies=allergies,
        dietary_restrictions=dietary_restrictions
    )

    if recipe.get("error") or not recipe.get("recipe_generated"):
        return recipe

    # Calculate nutrition
    nutrition = calculate_nutrition(ingredients)

    if "error" in nutrition:
        return nutrition

    # Check grocery budget
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

    # Create and save plan
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
