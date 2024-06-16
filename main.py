import subprocess
import os

def run_script(script_name, input_text):
    subprocess.run(['python', script_name, input_text])
    #process = subprocess.Popen(['python', script_name], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #output, error = process.communicate(input_text)
    #if error:
    #    print(f"Error in {script_name}: {error}")
    #return output


'''
# Step 1: Get dish suggestion based on ingredients
ingredients_input = "Suggest a dish based on these ingredients: tomatoes, cheese, basil"
dish_suggestion = run_script('ashioyajotham_chef.py', ingredients_input)
print(f"Dish suggestion: {dish_suggestion}")

# Step 2: Get recipe for the suggested dish
recipe_request_input = f"Give a detailed recipe for the dish: {dish_suggestion}"
recipe = run_script('abdul_abdi_chef.py', recipe_request_input)
print(f"Recipe: {recipe}")

# Step 3: Criticize the given recipe
critique_request_input = f"Criticize the following recipe: {recipe}"
critique = run_script('asad_chef.py', critique_request_input)
print(f"Critique: {critique}")

'''
while True:
    print("\n -------------------------------------------------------------------------------------------------\n")
    print("Welcome to the Chef Assistant. What would you like to do?")
    print("These are the chef names and their specialities to choose from:")
    print("\n\
        Yogesh - Indian Yoga & Ayurveda\n\
        Ashioyajotham - African Cuisine\n\
        Dfst - Mexican Cuisine\n\
        Rahu - Indian Vegetarian Cuisine\n\
        Asad - Italian Cuisine\n\
        Abdul - Arabic Cuisine\n\
        Exit - To exit\n\
        ")

    print("Enter Chef Name:")
    chef_name = input().lower()
    if chef_name == 'exit' or chef_name == '':
        print("Thank you for using the Chef Assistant. Goodbye!")
        break
    if chef_name not in ['yogesh', 'ashioyajotham', 'dfst', 'rahu', 'asad', 'abdul']:
        print("Invalid input. Please enter a valid chef name.")
        continue
    print("Select one of the following options for:\n\
                    1. provide ingredients to suggest a dish name\n\
                    2. provide a dish name to get a detailed recipe\n\
                    3. Provide a recipe for a dish to get a critique of it and get suggestions to improve it\
                    ")
    user_input = input()
    if user_input not in ['1', '2', '3']:
        print("Invalid input. Please enter a valid option.")
        continue
    if user_input == '1':
        print("Enter Ingredients:")
        user_input = "ingredient:" + ' ' + input()
    elif user_input == '2':
        print("Enter Dish Name:")
        user_input = "recipe for:" + ' ' + input()
    elif user_input == '3':
        print("Enter Recipe:")
        user_input = "criticize recipe:" + ' ' + input()

    print("##############   This is your chef:" + ' ' + chef_name + '   ##############')
    dish_suggestion = run_script(chef_name + '_chef.py', user_input)
