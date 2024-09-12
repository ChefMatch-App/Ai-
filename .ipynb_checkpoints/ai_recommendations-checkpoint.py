{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bb25d5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def hybrid_recommendation(user_id, meal_id, alpha=0.7, top_n=5):\n",
    "    #  SVD recommendations\n",
    "    svd_recipes = get_svd_recommendations(user_id, top_n * 3) \n",
    "\n",
    "    #  content-based recommendations\n",
    "    content_based_recipes = get_content_based_recommendations(meal_id, top_n * 2)\n",
    "    \n",
    "   \n",
    "    svd_scores = {rec: model.predict(user_id, rec).est for rec in svd_recipes}\n",
    "    content_scores = {rec: cosine_sim[recipe2idx[meal_id], recipe2idx[rec]] for rec in content_based_recipes}\n",
    "    \n",
    "    # scores\n",
    "    combined_scores = {}\n",
    "    for meal in set(svd_scores.keys()).union(content_scores.keys()):\n",
    "        svd_score = svd_scores.get(meal, 0)\n",
    "        content_score = content_scores.get(meal, 0)\n",
    "        combined_score = alpha * svd_score + (1 - alpha) * content_score\n",
    "        combined_scores[meal] = combined_score\n",
    "    \n",
    "    # Sort recipes based on combined scores\n",
    "    sorted_recipes = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)\n",
    "    \n",
    "    # Get top N meal IDs\n",
    "    top_meals = [meal[0] for meal in sorted_recipes[:top_n]]\n",
    "    \n",
    "    # Fetch details for top meals\n",
    "    recommendations = df[df['meal_id'].isin(top_meals)][['meal_id', 'recipe_name', 'restaurant']]\n",
    "    \n",
    "    return recommendations\n",
    "\n",
    "\n",
    "print(hybrid_recommendation(user_id=1, meal_id=1533.0))  \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
