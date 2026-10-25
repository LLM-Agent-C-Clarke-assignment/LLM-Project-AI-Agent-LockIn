
def nutrition_tool(ingredients):
    """
    Calculate nutrition using values supplied by the user.

    Example:
    ingredients = [
        {
            "name": "rice",
            "calories": 130,
            "protein": 2.7,
            "carbs": 28,
            "fat": 0.3,
            "quantity": 200
        }
    ]
    """

    total = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0
    }

    for item in ingredients:
        quantity = item["quantity"] / 100

        total["calories"] += item["calories"] * quantity
        total["protein"] += item["protein"] * quantity
        total["carbs"] += item["carbs"] * quantity
        total["fat"] += item["fat"] * quantity

    return {
        key: round(value, 2)
        for key, value in total.items()
    }
