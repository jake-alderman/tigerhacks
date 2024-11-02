from functions import makeFoodObjects, calculateBMI, getInfo


Meats = [['Chicken',165,3.5], ['Steak',155,3.5], ['Salmon',175,3.5], ['Beef',210,3.5]]
#rice, pasta, bread, tortilla
Carbs = [['Rice',205,8], ['Pasta',200,8], ['Bread',150,2], ['Tortilla',200,2]]
#Broccoli, carrot, corn, lettuce
Vegetables = [['Broccoli',31,8], ['Carrot',50,8], ['Corn',90,4], ['Lettuce',10,8]]      
#Apple, Banana, Strawberry, Orange        
Fruits = [['Apple',95,9], ['Banana',110,4.5], ['Strawberry',45,8], ['Orange',73,6]] 


meat = makeFoodObjects(Meats)
carb = makeFoodObjects(Carbs)
vegetable = makeFoodObjects(Vegetables)
fruit = makeFoodObjects(Fruits)


for food in meat:
    print(food.getName())
for food in carb:
    print(food.getName())
for food in vegetable:
    print(food.getName())

for food in fruit:
    print(food.getName())

#print(calculateBMI(67,135))
#getInfo()
