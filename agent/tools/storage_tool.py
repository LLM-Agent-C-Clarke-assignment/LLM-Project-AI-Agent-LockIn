
import json
import os


def save_meal_plan(meal_plan):
    """Save a meal plan to a JSON file."""

    if not meal_plan:
        return {"error": "Meal plan is empty."}

    
    os.makedirs("saved_plans", exist_ok=True)

   
    files = os.listdir("saved_plans")
    plan_number = len(files) + 1

    
    file_name = f"meal_plan_{plan_number}.json"
    file_path = os.path.join("saved_plans", file_name)


    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(meal_plan, file, indent=4)

        return {
            "success": True,
            "message": "Meal plan saved successfully.",
            "file_name": file_name
        }

    except (OSError, TypeError, ValueError) as error:
        return {"error": str(error)}
