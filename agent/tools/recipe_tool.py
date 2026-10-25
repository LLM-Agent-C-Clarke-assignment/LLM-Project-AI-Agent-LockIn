
def check_recipe_suitability(
    ingredients,
    allergies=None,
    dietary_restrictions=None
):
    """Check recipe ingredients against declared allergies and diets."""

    allergies = [
        item.strip().lower() for item in (allergies or [])
    ]
    dietary_restrictions = [
        item.strip().lower()
        for item in (dietary_restrictions or [])
    ]

    if not ingredients:
        return {"error": "Ingredients list is empty."}

    # Ingredient names and their common forms.
    allergen_groups = {
        "peanuts": [
            "peanut", "groundnut"
        ],
        "tree nuts": [
            "almond", "cashew", "walnut", "pistachio",
            "hazelnut", "pecan", "macadamia", "brazil nut"
        ],
        "milk": [
            "milk", "butter", "cheese", "cream",
            "yogurt", "ghee", "whey", "casein"
        ],
        "eggs": [
            "egg", "mayonnaise"
        ],
        "fish": [
            "fish", "salmon", "tuna", "cod", "sardine"
        ],
        "shellfish": [
            "prawn", "shrimp", "crab", "lobster", "clam",
            "oyster", "mussel", "scallop"
        ],
        "soy": [
            "soy", "soya", "tofu", "tempeh", "edamame"
        ],
        "wheat": [
            "wheat", "flour", "semolina", "bulgur", "seitan"
        ],
        "sesame": [
            "sesame", "tahini"
        ]
    }

    # Dietary restrictions use exact ingredient names.
    meat = {
        "chicken", "beef", "pork", "mutton", "lamb",
        "turkey", "bacon", "ham"
    }
    fish = {
        "fish", "salmon", "tuna", "sardine", "cod",
        "prawn", "shrimp", "crab", "lobster", "squid"
    }
    dairy = {
        "milk", "butter", "cheese", "cream", "yogurt",
        "ghee", "whey", "casein"
    }
    eggs = {"egg", "eggs", "mayonnaise"}
    gluten_grains = {
        "wheat", "barley", "rye", "semolina", "bulgur",
        "couscous", "seitan"
    }

    names = []

    for item in ingredients:
        if isinstance(item, dict):
            name = item.get("name", "")
        else:
            name = item

        if not isinstance(name, str) or not name.strip():
            return {"error": "Every ingredient must have a valid name."}

        names.append(name.strip().lower())

    allergy_conflicts = []
    dietary_conflicts = []

    # Check declared allergies.
    for allergy in allergies:
        if allergy not in allergen_groups:
            allergy_conflicts.append(
                f"Allergy '{allergy}' is not supported by this checker."
            )
            continue

        terms = allergen_groups[allergy]

        for ingredient in names:
            # Conservative matching: any mention of a known allergen
            # term triggers a warning.
            if any(term in ingredient for term in terms):
                allergy_conflicts.append(
                    f"{ingredient} may contain the allergen: {allergy}"
                )

    # Check dietary restrictions.
    for restriction in dietary_restrictions:
        for ingredient in names:
            conflict = False

            if restriction == "vegan":
                conflict = (
                    ingredient in meat
                    or ingredient in fish
                    or ingredient in dairy
                    or ingredient in eggs
                    or ingredient in {"honey"}
                )

            elif restriction == "vegetarian":
                conflict = (
                    ingredient in meat
                    or ingredient in fish
                )

            elif restriction in {"dairy-free", "dairy free"}:
                conflict = ingredient in dairy

            elif restriction in {"gluten-free", "gluten free"}:
                conflict = any(
                    grain in ingredient for grain in gluten_grains
                )

            elif restriction in {"egg-free", "egg free"}:
                conflict = ingredient in eggs

            elif restriction in {"pescatarian"}:
                conflict = ingredient in meat

            else:
                dietary_conflicts.append(
                    f"Restriction '{restriction}' is not supported."
                )
                break

            if conflict:
                dietary_conflicts.append(
                    f"{ingredient} conflicts with {restriction}"
                )

    # Do not describe the recipe as guaranteed safe.
    suitable = not allergy_conflicts and not dietary_conflicts

    return {
        "suitable_based_on_known_ingredients": suitable,
        "allergy_conflicts": sorted(set(allergy_conflicts)),
        "dietary_conflicts": sorted(set(dietary_conflicts)),
        "ingredients_checked": names,
        "warning": (
            "This is only a basic ingredient screening tool. "
            "Verify product labels, hidden ingredients and "
            "cross-contact risks. It cannot guarantee allergy safety."
        )
    }


def recipe_tool(
    ingredients,
    allergies=None,
    dietary_restrictions=None
):
    """Generate a basic recipe and check its suitability."""

    if not ingredients:
        return {"error": "Please provide ingredients."}

    suitability = check_recipe_suitability(
        ingredients,
        allergies,
        dietary_restrictions
    )

    if "error" in suitability:
        return suitability

    if not suitability["suitable_based_on_known_ingredients"]:
        return {
            "recipe_generated": False,
            "message": "Recipe rejected due to potential conflicts.",
            "suitability": suitability
        }

    return {
        "recipe_generated": True,
        "recipe_name": f"Simple {ingredients[0]['name'].title() if isinstance(ingredients[0], dict) else str(ingredients[0]).title()} Meal",
        "ingredients": ingredients,
        "instructions": [
            "Wash and prepare the ingredients.",
            "Cook the ingredients using a suitable method.",
            "Check that food is thoroughly cooked.",
            "Serve fresh."
        ],
        "suitability": suitability
    }
