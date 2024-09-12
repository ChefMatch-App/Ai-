import pickle
import numpy as np
import pandas as pd

# Load the recommendation model from the pickle file
with open('hybrid_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load meal data from an Excel file
meal_data = pd.read_excel('meals.xlsx', engine='openpyxl')

def recommend_meal(user_id: int, rating: float):
    # Prepare the input data (this depends on your model's expected input format)
    input_data = np.array([[user_id, rating]])

    # Make a prediction
    meal_id_pred = model.predict(input_data)[0]  # Get the first prediction

    # Get the meal name and ID from the meal data
    meal_info = meal_data[meal_data['meal_id'] == meal_id_pred].iloc[0]
    return {
        'meal_name': meal_info['meal_name'],
        'meal_id': meal_info['meal_id']
    }
