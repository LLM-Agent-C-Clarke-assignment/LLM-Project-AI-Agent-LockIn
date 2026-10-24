# LLM-Project-AI-Agent-LockIn
NutriMind AI Agent
 <div align="center">

<img src="assets/logo.png" alt="NutriMind AI Logo" width="250">

# NutriMind AI

### Smart Nutrition • Better You

**Your Smart AI-Powered Nutrition & Meal Planning Assistant**

An AI-powered meal planning assistant that helps users discover recipes, calculate nutrition, manage grocery budgets, and save personalized meal plans.

</div>

---

## 📌 Project Overview

NutriMind AI is an AI agent designed to help users make better food choices based on their fitness goals, food preferences, allergies, dietary restrictions, and grocery budget.

The system uses a locally running Large Language Model (LLM) through Ollama. The agent can select and execute Python tools to complete tasks, process tool results, and generate useful responses.

The project demonstrates how an AI agent can interact with real Python functions, manage multi-step tasks, and store information for future use.

## 🎯 Project Objectives

- Build an AI agent using Python and Ollama.
- Generate personalized recipe and meal plan suggestions.
- Calculate nutrition information using a recipe dataset.
- Estimate grocery costs and manage a budget in Sri Lankan Rupees (LKR).
- Suggest alternative ingredients when appropriate.
- Save meal plans and related information.
- Demonstrate tool calling, multi-step reasoning, validation, and error handling.

## ✨ Key Features

- **Personalized Meal Planning:** Suggest recipes according to the user's fitness goal and preferences.
- **Fitness Goals:** Support goals such as weight loss, weight gain, and muscle building.
- **Food Preferences:** Consider preferred ingredients and food types.
- **Allergy and Dietary Restrictions:** Use the user's restrictions when selecting recipes.
- **Nutrition Calculation:** Calculate available nutrition information from the local dataset.
- **Grocery Budget Management:** Estimate costs and compare them with the user's budget.
- **Ingredient Substitution:** Suggest suitable alternatives when ingredients are unavailable or over budget.
- **Meal Plan Storage:** Save generated meal plans for later reference.
- **Tool-Call Trace:** Display tool names, arguments, and results during agent execution.
- **Input Validation:** Validate user inputs and handle invalid data or missing files.
- **Local AI Model:** Use Ollama to run the language model locally.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic and tools |
| Ollama | Run the local language model |
| Llama 3.2 | Generate AI responses |
| LangChain | Connect the model with tools |
| LangGraph | Organize the agent workflow |
| Streamlit | Build the user interface |
| JSON | Store recipe and price datasets |
| SQLite | Store structured application data |
| CSS | Customize the user interface |
| Git and GitHub | Version control and collaboration |

## 🤖 Python Tools

The agent uses Python tools to perform real operations rather than simply describing what it would do.

### 1. `get_food_suggestions()` Recipe Tool

Suggests suitable recipes based on the user's fitness goal, food preferences, allergies, dietary restrictions, and available ingredients.

### 2. `calculate_nutrition()`Nutrition Tool

Calculates nutrition values using available recipe data. Results depend on the completeness and accuracy of the dataset.

### 3. `manage_grocery_budget()` Budget Tool

Estimates grocery costs using the available price dataset and compares the estimated total with the user's budget in LKR.
 
### 4. `save_meal_plan()`  Storage Tool

Saves the generated meal plan and related information for later use.

## 🔄 Agent Workflow

1. The user enters their meal-planning requirements through the Streamlit interface.
2. The request is passed to the AI agent.
3. The model determines which tool or tools are needed.
4. Python executes the selected tool with its arguments.
5. Tool results are returned to the agent.
6. The agent may execute additional tools when required.
7. The agent generates a final response using the available results.
8. The meal plan can be saved for future reference.

The agent should use a configurable maximum number of steps to prevent an endless tool-calling loop. Tool calls, arguments, results, and errors should be logged for debugging and demonstration.

## 📂 Project Structure

```text
NutriMind-AI/
├── app.py
├── agent.py
├── tools.py
├── database.py
├── styles.css
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── recipes.json
│   └── prices.json
├── assets/
│   └── logo.png
└── saved_plans/
```

**File descriptions:**

- `app.py` — Streamlit user interface.
- `agent.py` — AI agent logic and tool-calling workflow.
- `tools.py` — Python tool implementations.
- `database.py` — Saving and retrieving application data.
- `styles.css` — Custom interface styling.
- `requirements.txt` — Python package dependencies.
- `data/recipes.json` — Recipe and nutrition dataset.
- `data/prices.json` — Ingredient price dataset.
- `assets/logo.png` — Project logo.
- `saved_plans/` — Directory for saved meal plans, if file-based storage is used.

*The structure above describes the intended organization; adjust it to match the actual files in the repository.*

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version supported by the selected packages.
- Ollama installed on the computer.
- Git installed.
- The required project files and datasets.

### Step 1: Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_FOLDER>
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### Step 3: Install Python dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 4: Download the Ollama model

Make sure Ollama is installed and running, then execute:

```bash
ollama pull llama3.2
```

To check that the model is available:

```bash
ollama list
```

### Step 5: Run the application

```bash
streamlit run app.py
```

Open the local address displayed in the terminal.

## 💬 Example User Prompts

### Prompt 1 — Weight Loss

> Create a meal plan for weight loss based on my food preferences and allergies. Suggest suitable recipes.

### Prompt 2 — Grocery Budget

> Create a healthy meal plan for muscle building within my LKR 5,000 grocery budget. Check the estimated costs and suggest cheaper alternatives if needed.

### Prompt 3 — Multi-Step Agent Task

> Create a three-day meal plan for weight loss using my available ingredients. Suggest recipes, calculate nutrition using the dataset, estimate grocery costs, check my budget, and save the final plan.

These prompts are examples. Their results depend on the tools, input fields, datasets, and features implemented in the application.

## 🧪 Testing and Demonstration

The project should be tested with:

- Valid user inputs and different fitness goals.
- Different food preferences and available ingredients.
- Allergy and dietary restriction scenarios.
- Grocery budgets that are sufficient and insufficient.
- Missing or invalid dataset entries.
- Tool execution errors and unavailable model scenarios.
- Saving and retrieving meal plans.

The demonstration video should be **3–5 minutes long** and show at least two complete tasks, including one multi-step request. Keep the tool-call trace visible so the viewer can see how the agent selects tools, passes arguments, receives results, and produces its final answer.

## 🛡️ Validation and Error Handling

The application should validate required inputs, check budget values, handle missing recipe or price data, and report tool failures clearly.

The agent should have a maximum step limit to avoid repeated tool calls. Tool outputs should be checked before being used in subsequent steps.

Nutrition and cost estimates are only as reliable as the underlying datasets. The application should not invent missing nutrition values or claim that estimated grocery prices are guaranteed current prices.

## 💾 Data Storage

Recipe and ingredient information can be maintained in JSON files. SQLite can be used to store meal plans and other structured application records.

Saved data should use a consistent format and handle missing or corrupted records gracefully. User secrets, private credentials, and local environment files must not be committed to the repository.

## 👥 Team Contributions

Complete this section with the actual work completed by each team member.

| Team member | Contribution |
|---|---|
| Member 1 | [Add actual contribution] |
| Member 2 | [Add actual contribution] |
Update the table to match your team's size and actual contributions.

## ⚠️ Limitations

- Recommendations depend on the available recipe dataset and local model.
- Ingredient prices may not reflect current market prices.
- Nutrition calculations depend on the accuracy and completeness of stored data.
- The AI model may occasionally generate incorrect or unsuitable suggestions.
- This application is a meal-planning aid and is not a replacement for professional medical or dietary advice.

## 🚀 Future Improvements

- Expand the recipe and ingredient database.
- Add more accurate local grocery prices.
- Improve allergy and dietary restriction checks.
- Add weekly meal-plan history and editing.
- Improve substitution recommendations.
- Add multilingual support.
- Introduce user accounts and personalized saved plans.
- Improve automated testing and deployment.

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Create a branch for your changes.
2. Implement and test your changes.
3. Commit your changes with a descriptive message.
4. Push your branch to GitHub.
5. Open a pull request if required by your team's workflow.

## 📄 Disclaimer

NutriMind AI is an educational project demonstrating AI agents and Python tool integration. Recipe suggestions, nutrition values, and grocery costs depend on the supplied datasets and should be independently verified before making important dietary or purchasing decisions.

---

<div align="center">

**NutriMind AI — Smart Nutrition • Better You**

</div>
