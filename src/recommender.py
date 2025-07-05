import pandas as pd
import random

def load_food_data(csv_path):
    return pd.read_csv(csv_path)

def recommend_meals(food_df, target_calories):
    meals = {'Breakfast': [], 'Lunch': [], 'Snacks': [], 'Dinner': []}
    total_calories = 0

    per_meal_target = target_calories / 4

    for meal_type in meals:
        meal_items = food_df[food_df['Type'] == meal_type].sample(frac=1).reset_index(drop=True)  # shuffle
        used_items = set()
        meal_cal = 0

        for idx, item in meal_items.iterrows():
            food_name = item['Food']

            if food_name in used_items: # to skip repeat item
                continue

            if meal_cal + item['Calories'] <= per_meal_target + 50:
                meals[meal_type].append(item)
                meal_cal += item['Calories']
                total_calories += item['Calories']
                used_items.add(food_name)

            if meal_cal >= per_meal_target:
                break

    return meals, total_calories