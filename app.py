# app.py

from src.calculator import calculate_bmi, estimate_calories
from src.recommender import load_food_data, recommend_meals

def main():
    print("Personalized Diet Recommender")
    print("-" * 40)

    # Step 1: Take user input
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (M/F): ")
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))
    activity_level = input("Activity level (low/medium/high): ").lower()
    goal = input("Your goal (weight_loss/maintain/weight_gain): ").lower()

    # Step 2: BMI + calorie estimation
    bmi = calculate_bmi(weight, height)
    calories = estimate_calories(bmi, activity_level, goal)

    print(f"\nYour BMI is: {bmi}")
    print(f"Recommended daily calories: {calories} kcal")

    # Step 3: Load food dataset
    food_df = load_food_data("data/indian_food_nutrition.csv")

    # Step 4: Recommend meals
    meals, total = recommend_meals(food_df, calories)

    # Step 5: Show recommended diet plan
    print("\nYour Personalized Diet Plan:\n")

    for meal_type, items in meals.items():
        print(f"{meal_type}:")
        for item in items:
            print(f"  - {item['Food']} ({item['Calories']} kcal)")
        print()

    print(f"Total Calories from meals: {total} kcal (target: {calories} kcal)\n")

if __name__ == "__main__":
    main()
