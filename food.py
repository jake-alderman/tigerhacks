class Food:
    def __init__(self, name, calories, ounces):
        self.name = name
        self.calories = calories
        self.ounces = ounces

    def getName(self):
        return self.name
    
    def getCalories(self):
        return self.calories
    
    def getOUnces(self):
        return self.ounces