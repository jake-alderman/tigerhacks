from food import Food

def makeFoodObjects(foodList):
    foodObjects = []
    for foods in foodList:
        food = Food(*foods)
        foodObjects.append(food)

    return foodObjects

def calculateBMI(height, weight):
    return weight * 703 / height /height


def getInfo():

    age = input("what is your age (years): ")
    while age.isdigit() == False:
        height = input("invalid input only integer: ")
    gender = input("whats your gender (m/f): ")
    while gender != "m" and gender != "f":
        gender = input("invalid input, only (m/f): ")
    weight = input("what is your weight (lbs): ")
    while weight.isdigit() == False:
        weight = input("invalid input only integer: ")
        
    height = input("what is your height (inches): ")
    while height.isdigit() == False:
        height = input("invalid input only integer: ")

    activityLevel = input("what is your activity level (1-5): ")
    while activityLevel.isdigit() == False or int(activityLevel) < 1 or int(activityLevel) > 5:
        activityLevel = input("invalid input only integer between 1 and 5: ")

    goalWeight = input("what is your goal weight (lbs): ")
    while goalWeight.isdigit() == False:
        goalWeight = input("invalid input only integer: ")
    timeline = input("how many weeks do you want to diet: ")
    while timeline.isdigit() == False:
        timeline = input("invalid input only integer: ")

    return [gender, weight, height, activityLevel, goalWeight, timeline, age]

def calculatebmr(gender, age, weight, height):
    if gender.lower() == 'm':
        return (10 * float(weight)) + (6.25 * float(height)) - (5 * float(age)) + 5
    elif gender.lower() == 'f':
        return (10 * float(weight)) + (6.25 * float(height)) - (5 * float(age)) - 161

def calculate_caloric_maintenance(bmr, activity_level):
    activity_multipliers = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
    }
    
    if activity_level in activity_multipliers:
        return float(bmr) * activity_multipliers[activity_level]
    else:
        print('na')


#divide pounds wanting to lose by weeks 
#to lose a pound a week you have to be in 500 deficite per day 
def calculateDeficit(maintnence, timeline, goalweight, weight):
    goal = int(weight) - int(goalweight)
    lbs = float(goal) / float(timeline)

    defPerDay = float(lbs) * 3500 / (7)

    return float(maintnence) - defPerDay


