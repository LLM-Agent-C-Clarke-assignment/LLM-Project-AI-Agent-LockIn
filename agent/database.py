
import sqlite3


def connect_db():
    return sqlite3.connect("meal_plans.db")


def create_table():
    with connect_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS meal_plans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                plan TEXT
            )
        """)


def save_plan(plan):
    try:
        with connect_db() as conn:
            conn.execute(
                "INSERT INTO meal_plans (plan) VALUES (?)",
                (str(plan),)
            )

        return {"success": True, "message": "Plan saved."}

    except sqlite3.Error as error:
        return {"error": str(error)}


def get_plans():
    with connect_db() as conn:
        rows = conn.execute(
            "SELECT * FROM meal_plans"
        ).fetchall()

    return rows
