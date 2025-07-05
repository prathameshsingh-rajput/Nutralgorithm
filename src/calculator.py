def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def estimate_calories(bmi, activity_level, goal):
    if activity_level == "low":
        base_cal = 1800
    elif activity_level == "medium":
        base_cal = 2200
    else:
        base_cal = 2600

    if goal == "weight_loss":
        return base_cal - 400
    elif goal == "weight_gain":
        return base_cal + 300
    else:
        return base_cal
