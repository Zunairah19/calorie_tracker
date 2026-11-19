from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
foods = []
settings = {"goal": 2000}

CATEGORIES = ["Breakfast", "Lunch", "Dinner", "Snack"]
ICONS = {"Breakfast": "🍳", "Lunch": "🍛", "Dinner": "🍽️", "Snack": "🍎"}


@app.route("/")
def index():
    total = sum(item["calories"] for item in foods)
    goal = settings["goal"]
    remaining = goal - total
    percent = min(int(total / goal * 100), 100) if goal > 0 else 0

    if total > goal:
        status = "over"
    elif percent >= 80:
        status = "warn"
    else:
        status = "good"

    by_category = {
        c: sum(i["calories"] for i in foods if i["category"] == c)
        for c in CATEGORIES
    }

    return render_template(
        "index.html",
        foods=foods,
        total=total,
        goal=goal,
        remaining=remaining,
        percent=percent,
        status=status,
        categories=CATEGORIES,
        icons=ICONS,
        by_category=by_category,
    )


@app.route("/add", methods=["POST"])
def add_food():
    name = request.form.get("name", "").strip()
    calories = request.form.get("calories", "").strip()
    category = request.form.get("category", "Snack")

    if category not in CATEGORIES:
        category = "Snack"

    if name and calories.isdigit():
        foods.append({"name": name, "calories": int(calories), "category": category})

    return redirect(url_for("index"))


@app.route("/delete/<int:index>", methods=["POST"])
def delete_food(index):
    if 0 <= index < len(foods):
        foods.pop(index)
    return redirect(url_for("index"))


@app.route("/goal", methods=["POST"])
def set_goal():
    goal = request.form.get("goal", "").strip()
    if goal.isdigit() and int(goal) > 0:
        settings["goal"] = int(goal)
    return redirect(url_for("index"))


@app.route("/clear", methods=["POST"])
def clear_foods():
    foods.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)