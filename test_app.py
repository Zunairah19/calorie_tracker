from app import app, foods


def setup_function():
    foods.clear()


def test_home_page_loads():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Calorie Tracker" in response.data


def test_add_food():
    client = app.test_client()
    client.post("/add", data={"name": "Apple", "calories": "95", "category": "Snack"})
    assert len(foods) == 1
    assert foods[0]["name"] == "Apple"
    assert foods[0]["calories"] == 95


def test_total_calories():
    client = app.test_client()
    client.post("/add", data={"name": "Apple", "calories": "95", "category": "Snack"})
    client.post("/add", data={"name": "Rice", "calories": "200", "category": "Lunch"})
    response = client.get("/")
    assert b"295" in response.data


def test_delete_food():
    client = app.test_client()
    client.post("/add", data={"name": "Apple", "calories": "95", "category": "Snack"})
    client.post("/delete/0")
    assert len(foods) == 0