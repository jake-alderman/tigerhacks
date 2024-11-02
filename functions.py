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
    gender = input("whats your gender (m/f)")
    while gender != "m" and gender != "m":
        gender = input("invalid input, only (m/f)")
    weight = input("what is your weight (lbs)")
    height = input("what is your height (inches)")
    activityLevel = input("what is your activity level (1-5)")
    goalWeight = input("what is your goal weight")
    timeline = input("how many weeks do you want to diet")
