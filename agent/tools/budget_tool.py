
import json


def load_prices():
    """Load ingredient prices from the JSON file."""

    with open("data/prices.json", "r", encoding="utf-8") as file:
        return json.load(file)


def calculate_total(ingredients, prices):
    """Calculate the total cost of ingredients."""

    total = 0

    for item in ingredients:
        name = item["name"].strip().lower()
        quantity = float(item["quantity"])

        if name not in prices:
            raise ValueError(f"Price not available for {name}")

        price = prices[name]["price_per_kg"]
        total += price * quantity

    return round(total, 2)


def manage_grocery_budget(ingredients, budget):
    """Check whether the grocery cost fits the budget."""

    if budget < 0:
        return {"error": "Budget cannot be negative."}

    try:
        prices = load_prices()
        total = calculate_total(ingredients, prices)

        return {
            "total_cost": total,
            "budget": budget,
            "within_budget": total <= budget,
            "remaining_budget": round(budget - total, 2)
        }

    except (ValueError, KeyError, TypeError, OSError) as error:
        return {"error": str(error)}
