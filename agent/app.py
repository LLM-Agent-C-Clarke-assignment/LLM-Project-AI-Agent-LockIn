import streamlit as st


st.set_page_config(
    page_title="NutriChef AI",
    page_icon="🥗",
    layout="wide"
)

def load_css():
    with open("style.css", "r", encoding="utf-8") as file:
        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.title("🥗 NutriChef AI")
st.write("Your personal AI meal planning assistant")

st.header("Create Your Meal Plan")


goal = st.selectbox(
    "Choose your fitness goal",
    ["Weight Loss", "Muscle Gain", "Weight Gain", "Healthy Eating"]
)


preferences = st.multiselect(
    "Food preferences",
    ["Chicken", "Fish", "Eggs", "Vegetables", "Rice", "Fruits"]
)


allergies = st.multiselect(
    "Select your allergies",
    ["Peanuts", "Milk", "Eggs", "Soy", "Fish", "Wheat"]
)


restrictions = st.multiselect(
    "Dietary restrictions",
    ["Vegetarian", "Vegan", "Halal", "Gluten-Free", "Dairy-Free"]
)

budget = st.number_input(
    "Your grocery budget (LKR)",
    min_value=0,
    value=5000,
    step=500
)

days = st.selectbox(
    "Meal plan duration",
    [1, 3, 5, 7]
)


pantry = st.text_input(
    "Ingredients you already have",
    placeholder="Rice, chicken, eggs"
)

if st.button("Generate Meal Plan"):
    if budget <= 0:
        st.error("Please enter a budget greater than zero.")

    else:
        user_request = {
            "goal": goal,
            "preferences": preferences,
            "allergies": allergies,
            "dietary_restrictions": restrictions,
            "budget": budget,
            "days": days,
            "pantry": [
                item.strip()
                for item in pantry.split(",")
                if item.strip()
            ]
        }

        st.subheader("Your Requirements")
        st.json(user_request)

        st.info(
            "Inputs are ready. Connect your AI agent "
            "in agent.py to generate the actual meal plan."
        )
