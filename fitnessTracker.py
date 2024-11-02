import customtkinter

class Food:
    def __init__(self, name, calories, ounces):
        self.name = name
        self.calories = calories
        self.ounces = ounces
        
    def getName(self):
        return self.name

    def getCalories(self):
        return self.calories
    
    def getOunces(self):
        return self.ounces

class Meal:
    def __init__(self, name):
        self.name = name
        self.foods = []
        
    def add_food(self, food):
        self.foods.append(food)
        
    def get_total_calories(self):
        return sum(food.getCalories() for food in self.foods)
    
    def get_food_list(self):
        return [food.getName() for food in self.foods]

def makeFoodObjects(food_list):
    return [Food(item[0], item[1], item[2]) for item in food_list]

class FitnessApp:
    def __init__(self):
        # Days tracking
        self.days = {
            "Day 1": {},
            "Day 2": {},
            "Day 3": {},
            "Day 4": {},
            "Day 5": {},
            "Day 6": {},
            "Day 7": {}
        }
        # Food Data with proper Food objects
        self.Meats = [['Chicken',165,3.5], ['Steak',155,3.5], ['Salmon',175,3.5], ['Beef',210,3.5]]
        self.Carbs = [['Rice',205,8], ['Pasta',200,8], ['Bread',150,2], ['Tortilla',200,2]]
        self.Vegetables = [['Broccoli',31,8], ['Carrot',50,8], ['Corn',90,4], ['Lettuce',10,8]]
        self.Fruits = [['Apple',95,9], ['Banana',110,4.5], ['Strawberry',45,8], ['Orange',73,6]]
        
        # Create food objects using the Food class
        self.meat = makeFoodObjects(self.Meats)
        self.carb = makeFoodObjects(self.Carbs)
        self.vegetable = makeFoodObjects(self.Vegetables)
        self.fruit = makeFoodObjects(self.Fruits)
        
        # Meal tracking
        self.current_day = "Day 1"
        self.meals = {
            "Breakfast": Meal("Breakfast"),
            "Lunch": Meal("Lunch"),
            "Dinner": Meal("Dinner"),
            "Snacks": Meal("Snacks")
        }
        
        # Setup GUI
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        
        self.root = customtkinter.CTk()
        self.root.geometry("800x700")
        self.root.title("Fitness Tracker")
        
        # Create tab view
        self.tab_view = customtkinter.CTkTabview(master=self.root)
        self.tab_view.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Add tabs
        self.tab_view.add("Caloric Calculator")
        self.tab_view.add("Food Selection")
        
        
        # Create food selection section in the Food Selection tab
        self.create_food_selection_frame()
        
        # Create calorie calculator section in the Caloric Calculator tab
        self.create_caloric_calculator_frame()
    
    def create_food_selection_frame(self):
        # Food selection frame
        food_frame = customtkinter.CTkFrame(master=self.tab_view.tab("Food Selection"))
        food_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Day selection
        self.day_var = customtkinter.StringVar(value="Day 1")
        day_menu = customtkinter.CTkOptionMenu(
            master=food_frame,
            values=list(self.days.keys()),
            variable=self.day_var,
            command=self.select_day
        )
        day_menu.pack(pady=5)
        
        # Food category selection
        self.food_var = customtkinter.StringVar(value="Select Category")
        food_categories = ["Meats", "Carbs", "Vegetables", "Fruits"]
        
        category_menu = customtkinter.CTkOptionMenu(
            master=food_frame,
            values=food_categories,
            variable=self.food_var,
            command=self.update_food_items
        )
        category_menu.pack(pady=5)
        
        # Food item selection
        self.food_item_var = customtkinter.StringVar(value="Select Food")
        self.food_item_menu = customtkinter.CTkOptionMenu(
            master=food_frame,
            values=["Select a category first"],
            variable=self.food_item_var,
            command=self.add_food_to_meal
        )
        self.food_item_menu.pack(pady=5)
        
        # Food info label
        self.food_info_label = customtkinter.CTkLabel(
            master=food_frame,
            text="Food information will appear here",
            font=("Helvetica", 12)
        )
        self.food_info_label.pack(pady=5)
        
        # Meal selection
        self.meal_var = customtkinter.StringVar(value="Select Meal")
        meal_menu = customtkinter.CTkOptionMenu(
            master=food_frame,
            values=list(self.meals.keys()),
            variable=self.meal_var
        )
        meal_menu.pack(pady=5)
        
        # Meal display labels
        self.meal_display_labels = {}
        for meal_name in self.meals.keys():
            meal_label = customtkinter.CTkLabel(
                master=food_frame,
                text=f"{meal_name}: No foods added\nTotal Calories: 0",
                font=("Helvetica", 14)
            )
            meal_label.pack(pady=5, padx=10, fill="x")
            self.meal_display_labels[meal_name] = meal_label
        
        # Total calorie display
        self.total_calories_label = customtkinter.CTkLabel(
            master=food_frame,
            text="Total Daily Calories: 0",
            font=("Helvetica", 18)
        )
        self.total_calories_label.pack(pady=12, padx=10)
        
        # Caloric Calculator Results Transfer Label
        self.caloric_results_label = customtkinter.CTkLabel(
            master=food_frame,
            text="Caloric Calculator Results will appear here",
            font=("Helvetica", 16)
        )
        self.caloric_results_label.pack(pady=12, padx=10)
    
    def create_caloric_calculator_frame(self):
        # Caloric calculator frame
        calc_frame = customtkinter.CTkFrame(master=self.tab_view.tab("Caloric Calculator"))
        calc_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Title
        label = customtkinter.CTkLabel(
            master=calc_frame, 
            text="Caloric Calculator",
            font=("Helvetica", 24)
        )
        label.pack(pady=12, padx=10)
        
        # Input fields
        self.create_input_fields(calc_frame)
        
        # Calculate button
        calculate_button = customtkinter.CTkButton(
            master=calc_frame,
            text="Calculate",
            command=self.calculate
        )
        calculate_button.pack(pady=12, padx=10)
        
        # Results label for calculations
        self.results_label = customtkinter.CTkLabel(
            master=calc_frame,
            text="Results will appear here",
            font=("Helvetica", 16)
        )
        self.results_label.pack(pady=12, padx=10)
    
    def create_input_fields(self, parent_frame):
        # Create entry fields
        self.entries = {}
        
        # Input fields with labels
        fields = [
            ('age', 'Age (years)'),
            ('gender', 'Gender (m/f)'),
            ('weight', 'Weight (lbs)'),
            ('height', 'Height (inches)'),
            ('activity', 'Activity Level (1-5)'),
            ('goal_weight', 'Goal Weight (lbs)'),
            ('timeline', 'Timeline (weeks)')
        ]
        
        for field_id, label_text in fields:
            frame = customtkinter.CTkFrame(master=parent_frame)
            frame.pack(pady=5, padx=10, fill="x")
            
            label = customtkinter.CTkLabel(
                master=frame,
                text=label_text,
                font=("Helvetica", 14)
            )
            label.pack(side="left", padx=10)
            
            entry = customtkinter.CTkEntry(master=frame)
            entry.pack(side="right", padx=10)
            
            self.entries[field_id] = entry
    
    def update_food_items(self, choice):
        # Get the appropriate food list based on category
        food_dict = {
            "Meats": self.meat,
            "Carbs": self.carb,
            "Vegetables": self.vegetable,
            "Fruits": self.fruit
        }
        
        selected_foods = food_dict.get(choice, [])
        food_names = [food.getName() for food in selected_foods]
        
        self.food_item_menu.configure(values=food_names)
        self.food_item_var.set("Select Food")
        self.food_info_label.configure(text="Select a food item")
    
    def select_day(self, day_name):
        self.current_day = day_name
        self.load_day_data()

    def add_food_to_meal(self, choice):
        # Reset food selection after adding
        # Find the selected food object
        category_dict = {
            "Meats": self.meat,
            "Carbs": self.carb,
            "Vegetables": self.vegetable,
            "Fruits": self.fruit
        }
        
        category = self.food_var.get()
        foods = category_dict.get(category, [])
        
        selected_food = next((food for food in foods if food.getName() == choice), None)
        
        if selected_food:
            # Add selected food to the current meal
            meal_name = self.meal_var.get()
            if meal_name in self.meals:
                self.meals[meal_name].add_food(selected_food)
                self.update_meal_display(meal_name)
            self.save_day_data()
            
            # Reset category and food selections after adding
            self.food_var.set("Select Category")
            self.food_item_var.set("Select Food")
            self.food_item_menu.configure(values=["Select a category first"])
            
            # Display food information
            info_text = f"""
Name: {selected_food.getName()}
Calories: {selected_food.getCalories()} per serving
Serving Size: {selected_food.getOunces()} oz
"""
            self.food_info_label.configure(text=info_text)
        
    def load_day_data(self):
        # Load meals for the selected day
        if self.current_day in self.days and self.days[self.current_day]:
            self.meals = self.days[self.current_day]
        else:
            self.meals = {
                "Breakfast": Meal("Breakfast"),
                "Lunch": Meal("Lunch"),
                "Dinner": Meal("Dinner"),
                "Snacks": Meal("Snacks")
            }
        
        # Update displays for all meals
        for meal_name in self.meals.keys():
            self.update_meal_display(meal_name)
        self.update_total_calories()

    def update_meal_display(self, meal_name):
        # Update meal display with foods and total calories
        meal = self.meals[meal_name]
        food_list = meal.get_food_list()
        total_calories = meal.get_total_calories()
        
        meal_display_text = f"{meal_name}:\n" + ", ".join(food_list) + f"\nTotal Calories: {total_calories}"
        self.meal_display_labels[meal_name].configure(text=meal_display_text)
        
        # Update total daily calories
        self.update_total_calories()
    
    def save_day_data(self):
        # Save current meals to the selected day
        self.days[self.current_day] = self.meals

    def update_total_calories(self):
        total_calories = sum(meal.get_total_calories() for meal in self.meals.values())
        self.total_calories_label.configure(text=f"Total Daily Calories: {total_calories}")
    
    def validate_inputs(self):
        try:
            age = int(self.entries['age'].get())
            gender = self.entries['gender'].get().lower()
            weight = float(self.entries['weight'].get())
            height = float(self.entries['height'].get())
            activity = int(self.entries['activity'].get())
            goal_weight = float(self.entries['goal_weight'].get())
            timeline = int(self.entries['timeline'].get())
            
            if not (0 < age < 120):
                return False, "Invalid age"
            if gender not in ['m', 'f']:
                return False, "Gender must be 'm' or 'f'"
            if not (50 < weight < 1000):
                return False, "Invalid weight"
            if not (36 < height < 96):
                return False, "Invalid height"
            if not (1 <= activity <= 5):
                return False, "Activity level must be between 1 and 5"
            if not (50 < goal_weight < 1000):
                return False, "Invalid goal weight"
            if not (1 <= timeline <= 52):
                return False, "Timeline must be between 1 and 52 weeks"
                
            return True, None
        except ValueError:
            return False, "Please fill all fields with valid numbers"

    def calculate(self):
        # Validate inputs
        valid, error_message = self.validate_inputs()
        if not valid:
            self.results_label.configure(text=f"Error: {error_message}")
            return
            
        # Get values
        gender = self.entries['gender'].get()
        age = int(self.entries['age'].get())
        weight = float(self.entries['weight'].get())
        height = float(self.entries['height'].get())
        activity_level = int(self.entries['activity'].get())
        goal_weight = float(self.entries['goal_weight'].get())
        timeline = int(self.entries['timeline'].get())
        
        # Calculate
        bmi = self.calculateBMI(height, weight)
        bmr = self.calculatebmr(gender, age, weight, height)
        maintenance_calories = self.calculate_caloric_maintenance(bmr, activity_level)
        target_calories = self.calculateDeficit(maintenance_calories, timeline, goal_weight, weight)
        
        # Display results
        results_text = f"""
BMI: {bmi:.1f}
BMR: {bmr:.0f} calories/day
Maintenance Calories: {maintenance_calories:.0f} calories/day
Target Daily Calories: {target_calories:.0f} calories/day
Weekly Weight Change: {(float(weight) - float(goal_weight)) / float(timeline):.1f} lbs/week
        """
        
        self.results_label.configure(text=results_text)
        self.caloric_results_label.configure(text=results_text)

    def calculateBMI(self, height, weight):
        return (weight * 703) / (height * height)

    def calculatebmr(self, gender, age, weight, height):
        if gender.lower() == 'm':
            return 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
        else:
            return 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)

    def calculate_caloric_maintenance(self, bmr, activity_level):
        activity_multipliers = {
            1: 1.2,  # Sedentary
            2: 1.375,  # Light activity
            3: 1.55,  # Moderate activity
            4: 1.725,  # Very active
            5: 1.9  # Extra active
        }
        return bmr * activity_multipliers.get(activity_level, 1.2)

    def calculateDeficit(self, maintenance_calories, timeline, goal_weight, current_weight):
        weight_to_lose = current_weight - goal_weight
        weekly_deficit = (weight_to_lose / timeline) * 3500  # 3500 calories = 1 pound
        daily_deficit = weekly_deficit / 7
        return maintenance_calories - daily_deficit

    def run(self):
        self.root.mainloop()

def main():
    app = FitnessApp()
    app.run()

if __name__ == "__main__":
    main()



