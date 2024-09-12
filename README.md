# Recipe Recommendation System API

## Overview

This API offers a recommendation system for recipes based on a hybrid model that combines content-based filtering (using recipe ingredients) and collaborative filtering (using user ratings). It allows users to obtain personalized recommendations and discover similar recipes.

## Features

- **Content-Based Filtering**: Recommends recipes based on similar ingredients.
- **Collaborative Filtering**: Suggests recipes based on user ratings, utilizing the SVD algorithm.
- **Hybrid Recommendations**: Combines content-based and collaborative filtering for a more personalized recommendation.
- **Batch Processing**: Efficiently computes cosine similarity in large datasets.

## Prerequisites

To run this API, you will need:

- Python 3.7+
- Required Python libraries:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `scipy`
  - `surprise`
- A dataset containing recipe information and user ratings. The dataset should include:
  - `recipe_name`
  - `user_id`
  - `meal_id`
  - `ingredients` (as a list or string)
  - `restaurant`
  - `city`
  - `rating`

## Setup Instructions

1. **Clone the Repository**: Download or clone this repository to your local machine.
   
2. **Install Dependencies**: Install the required Python packages by using the following command:
   
   ```bash
   pip install -r requirements.txt

# Recipe Recommendation System API

## Dataset

Ensure that your dataset is in a CSV format with the necessary columns as mentioned above. This will be used for both content-based filtering (ingredient analysis) and collaborative filtering (user rating predictions).

## Start the API

Run the application by using the provided script. The API will be available at the specified port. You can use tools like Postman or curl to test the endpoints.

## API Endpoints

### 1. Get Similar Recipes (Content-Based)
- **Endpoint**: `/similar_recipes`
- **Method**: `GET`
- **Description**: Returns recipes similar to a given recipe based on its ingredients.
- **Parameters**:
  - `meal_id` (required): The ID of the recipe to find similar recipes.
  - `top_n` (optional): The number of similar recipes to return (default is 5).

### 2. Get User-Based Recommendations (SVD)
- **Endpoint**: `/user_recommendations`
- **Method**: `GET`
- **Description**: Provides personalized recipe recommendations for a given user, based on their previous ratings.
- **Parameters**:
  - `user_id` (required): The ID of the user for whom the recommendations are generated.
  - `top_n` (optional): The number of recommended recipes to return (default is 5).

### 3. Hybrid Recommendations
- **Endpoint**: `/hybrid_recommendations`
- **Method**: `GET`
- **Description**: Combines content-based filtering and collaborative filtering to provide a hybrid recommendation for a specific user and meal.
- **Parameters**:
  - `user_id` (required): The ID of the user.
  - `meal_id` (required): The ID of the recipe.
  - `alpha` (optional): The weighting factor between content-based and collaborative filtering (default is 0.7).
  - `top_n` (optional): The number of top recommended recipes to return (default is 5).

### 4. Train Model
- **Endpoint**: `/train_model`
- **Method**: `POST`
- **Description**: Trains the collaborative filtering model (SVD) using the provided dataset. This endpoint should be used to update the model periodically as more user data is collected.

## Usage

### Start the API

Run the server locally or deploy it to a cloud service. Once the server is running, you can make requests to the API endpoints.

### Making Requests

Use tools like Postman, curl, or any HTTP client to interact with the API. Pass the necessary parameters in the request URL or body as required by each endpoint.

### Hybrid Recommendations

For the most personalized experience, use the `/hybrid_recommendations` endpoint, which combines the power of both content-based filtering (ingredient similarity) and collaborative filtering (user preference).

### Updating the Model

As more user data is gathered, re-train the model using the `/train_model` endpoint to keep the recommendations accurate and up-to-date.
