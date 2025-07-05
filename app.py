from flask import Flask, render_template, request
from src.calculator import calculate_bmi, estimate_calories
from src.recommender import load_food_data, recommend_meals

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/form')
def form():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    age = int(request.form['age'])
    gender = request.form['gender']
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    activity = request.form['activity']
    goal = request.form['goal']

    bmi = calculate_bmi(weight, height)
    calories = estimate_calories(bmi, activity, goal)

    food_data = load_food_data('data/food_dataset.csv')
    meals, total_calories = recommend_meals(food_data, calories)

    return render_template('result.html',
                           bmi=bmi,
                           calories=calories,
                           meals=meals,
                           total=total_calories,
                           user_data={
                               'age': age,
                               'gender': gender,
                               'weight': weight,
                               'height': height,
                               'activity': activity,
                               'goal': goal
                           })

if __name__ == '__main__':
    app.run(debug=True)
