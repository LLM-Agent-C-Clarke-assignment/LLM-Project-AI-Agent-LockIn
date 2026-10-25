
def calculate_nutrition(ingredients):
    """Calculate the total nutrition of ingredients."""

    if not ingredients:
        return {"error": "Ingredients list is empty."}

    total = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0
    }

    try:
        for item in ingredients:
            quantity = float(item["quantity"])

            if quantity < 0:
                return {"error": "Quantity cannot be negative."}

            for nutrient in total:
                value = float(item[nutrient])

                if value < 0:
                    return {
                        "error": f"{nutrient} cannot be negative."
                    }

                total[nutrient] += value * quantity / 100

        return {
            "total_calories": round(total["calories"], 2),
            "total_protein": round(total["protein"], 2),
            "total_carbs": round(total["carbs"], 2),
            "total_fat": round(total["fat"], 2)
        }

    except (KeyError, TypeError, ValueError) as error:
        return {"error": str(error)}

