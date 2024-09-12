from fastapi import FastAPI
from model import recommend_meal
from funcs import preprocess_input

# Initialize the FastAPI app
app = FastAPI()

@app.get('/')
def home():
    """
    A simple health check endpoint.
    """
    return {"health_check": "ok"}

@app.post("/recommend/")
async def recommend(user_id: int, rating: float):
    """
    Endpoint to recommend a meal based on UserID and rating input.
    """
    # Preprocess the input data
    user_id, rating = preprocess_input(user_id, rating)

    # Get meal recommendation
    meal_name, meal_id = recommend_meal(user_id, rating)

    # Return the meal name and its ID
    return {"meal_name": meal_name, "meal_id": meal_id}
