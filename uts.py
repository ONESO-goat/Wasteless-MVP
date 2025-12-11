import json


THE_FOOD = "load_users_and_their_food.json"
THE_USER = "the_people_using_app.json"
FLAGGED_USERS = {}
USER_POINTS = 0


# THE DATA FOR THE FOOD
def load_the_food(): # Load the data
  try:
    with open(THE_FOOD, 'r') as file: # THE FOOD
      return json.load(file)
  except FileNotFoundError:
    return {}
  
def save_the_food(data):
  with open(THE_FOOD, 'w') as file:
    json.dump(data, file, indent=4)



# THE DATA OF THE USERS IN THE PROGRAM
def load_the_users():
  try: 
    with open(THE_USER, 'r') as file: # THE USER
      return json.load(file)
  except FileNotFoundError:
    return {} 

def save_the_user(data):
  with open(THE_USER, 'w') as file:
    json.dump(data, file, indent=4)