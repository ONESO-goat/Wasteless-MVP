
import json
from datetime import datetime, timedelta
import time
import random



###SO THIS IS MY PROJECT FOR A SIMPLE MVP FOR MY FOOD APP IDEA

## FOR ME, ILL MAKE THE FUNCTIONS FIRST TO UNDERSTAND THE BASICS ILL NEED

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


def foods_inputed_by_user():
  return {
          "foods": [],
          "drinks": [],
          "snacks": [],
          "dates": [], # list of dates the habit was completed
          "flags": []
          }


def user_login():
  users = load_the_users()
  """THE USER LOG INS IF THEY ALREADY OWN AN ACCOUNT"""
  #attempts = 0
  the_max_attempts = 8

  while True:
    username = input("please insert username: ")

    if username not in users:
      print("this username doesn't exist")

    else:
      while True:
        password = input("please enter password: ")

        if password != users[username]["password"]:
          print("wrong password, please try again.")
          the_max_attempts -= 1
          if the_max_attempts <= 4:
            print(f"{the_max_attempts} attempts left.")

        else:
          print(f"Welcome back {username}!")
          return username, logged_into_the_system(username)

    if the_max_attempts == 0:
      print("too many attempts, please try again later.")
      break





def user_signUP():
  users = load_the_users()
  #i = foods_inputed_by_user()
  global USER_POINTS
  """USER SIGN UP"""
  while True:
    username_create = input("please enter your username: ")
    if username_create in users:
      print("Sorry that username is already taken, please try again") # maybe add a system that recommends usernames like the one given
    
    elif len(username_create) < 4:
      print("Usernames need a minimum of 4 characters, please try again.")

    else:
      while True:
        password_creation = input("Please enter vaild password: ")
        
        if len(password_creation) < 8:
          print("Please insert a minimun of 8 characters")
        elif password_creation.isalnum():
          print("Please include atleast 1 special charcter.")
        else:
          
          users[username_create] = {
            "password": password_creation,
            "foods": [],
            "drinks": [],
            "snacks": [],
            "user_points": 0,
            "user_status": [],
            "flags": []
          }

          save_the_user(users)
          
          

          
          print(f"Welcome {username_create.upper()}! We really like that you want to avoid wasting food! we hope...")
          time.sleep(1)
          print("Before we get started, let's learn more about you! What's in your frigde?") # ADD MORE TO THIS THE FUTURE
          return add_foods(username_create), username_create






 
def The_day_and_how_much_time_has_passed(data): # check the date and check how much time has passed
  ... # THIS MIGHT NEED MORE THAN ONE



def ranking_of_the_users(user): # THE MINI LEADERBOARD SYSTEM
  print()
  while True:
    users = load_the_users()
    if user not in users:
      user = 'Guest'
      print(f"Hello fellow {user.upper()}! Make an account to see even more on this page" + "\n" + "and better insight on what it takes to be on this list!")
    print("=========================")
    print("Our best users world wide")
    print("=========================")
    print()
    if user in users:
     # ch = users[user]['user_points']
      print(user)

    #print([usr for usr in users if users[usr]['user_points'] > all(users)])
    h = ([u for u in users])

      #print(sorted([usr for usr in users if users[usr]['user_points'] > all([usr for usr in users])]))

    for rank, (user, data) in enumerate(sorted(users.items(), key=lambda x: x[1]["user_points"],reverse=True),1):
        print(f"{rank}: {user}  {data['user_points']}")
       
# I WANT to pprint out the users, only the top 5 on the leaderboard.
    

    print()
    print("GO BACK (1)")
    r = input("")
    if r == '1' and user not in users:
      return main()
    else:
      return logged_into_the_system(user)
    
      # if users waste more food, they get a low rank


def mini_shop(user): # Prices vary on your ranking. 
  ...

def add_foods(user):
  #food = load_the_food()
  users = load_the_users()
  uuu = foods_inputed_by_user()
  print(f"hey {user}")
  while True:
      print("What's on your shopping list?")
      print()
      print("1: drinks")
      print("2: foods")
      print("3: snacks") 
      print("4: exit")
      print()
      user_choice = input("---> ") 
      if user_choice == '1':
        while True:
          the_food_or_drink_or_edible_of_any_kind_the_user_inputs = input("What's the amazing drink? (press 1 to exit) ")
          if the_food_or_drink_or_edible_of_any_kind_the_user_inputs == '1':
            return add_foods(user)
          elif len(the_food_or_drink_or_edible_of_any_kind_the_user_inputs) <= 3:
              print("too short, we don't know any drinks with wording less than 4 letters.")
          elif len(users[user]['drinks']) >= 3:
            print("Is it the end of the world? I would advice you to stay minimal on the drinks.") 
            FLAGGED_USERS["USER NAME: "] = user
            chay = 0
            issue = 'too many drinks'

            if issue in users[user]['flags']:
               #users[user]['flags'][issue] = chay
               pass
            else:
              users[user]['flags'].append(issue) 

            save_the_user(users)
            # ADD SYSTEM IN FUTURE WHERE THE USER TYPES HOW MANY PEOPLE ARE IN THEIR FAMILY, WOULD NEED PROOF OF THIS

          else:
            print(f"{the_food_or_drink_or_edible_of_any_kind_the_user_inputs} is added, don't forget check off items ounce you have them.")
            users[user]['drinks'].append(the_food_or_drink_or_edible_of_any_kind_the_user_inputs)
            save_the_user(users)
            print("Anymore?")
            print("1: YES")
            print("2: NO")
                
            choice = input("CHOICE: ")
            if choice == '1':
              continue
            else:
              return add_foods(user)
      



      elif user_choice == '2':
        while True:
          the_food_or_drink_or_edible_of_any_kind_the_user_inputs = input("What's the amazing meal? (press 1 to exit) ")
          if the_food_or_drink_or_edible_of_any_kind_the_user_inputs == '1':
              return add_foods(user)
          elif len(the_food_or_drink_or_edible_of_any_kind_the_user_inputs) < 4:
              print("too short, we don't know any foods with wording less than 4 letters.") # soon, add qr code reader
          
          elif len(users[user]['foods']) >= 3: # >= 10
            print("Is it the end of the world? I would advice you to stay minimal on the meals.") 
            FLAGGED_USERS["USER NAME: "] = user
            chay = 0
            issue_food = 'too many foods'

            if issue_food in users[user]['flags']:
               #users[user]['flags'][issue_food] = chay
               pass
            else:
              users[user]['flags'].append(issue_food)

            save_the_user(users)
            # ADD SYSTEM IN FUTURE WHERE THE USER TYPES HOW MANY PEOPLE ARE IN THEIR FAMILY, WOULD NEED PROOF OF THIS


          else:
            print(f"{the_food_or_drink_or_edible_of_any_kind_the_user_inputs} is added, don't forget check off items ounce you have them.")
            users[user]['foods'].append(the_food_or_drink_or_edible_of_any_kind_the_user_inputs)
            save_the_user(users)
            
            print("Anymore?")
            print("1: YES")
            print("2: NO")
                  
            choice = input("CHOICE: ")
            if choice == '1':
              continue
            else:
              return add_foods(user)



      elif user_choice == '3':
        while True:
          the_food_or_drink_or_edible_of_any_kind_the_user_inputs = input("What's the amazing snack being bought? (Don't say the brand just say it's type, EX: Candy, Chips, Popcorn?): ")
          print("(print 1 to exit)")
          if the_food_or_drink_or_edible_of_any_kind_the_user_inputs == '1':
              return add_foods(user)
          elif len(the_food_or_drink_or_edible_of_any_kind_the_user_inputs) <= 3:
              print("too short, we don't know any snack with wording less than 4 letters.")
          
          elif len(users[user]['snacks']) >= 3:
            print("Whoa! Have room for real food my friend.") 
            FLAGGED_USERS["USER NAME: "] = user
            chay = 0
            issue_snacks = 'too many snacks'

            if issue_snacks in users[user]['flags']:
               pass
            else:
              users[user]['flags'].append(issue_snacks)

            save_the_user(users)
            # ADD SYSTEM IN FUTURE WHERE THE USER TYPES HOW MANY PEOPLE ARE IN THEIR FAMILY, WOULD NEED PROOF OF THIS

          else:
            print(f"{the_food_or_drink_or_edible_of_any_kind_the_user_inputs} is added, don't forget check off items ounce you have them.")
            users[user]['snacks'].append(the_food_or_drink_or_edible_of_any_kind_the_user_inputs)
            save_the_user(users)
            print("Anymore?")
            print("1: YES")
            print("2: NO")
                  
            choice = input("CHOICE: ")
            if choice == '1':
                continue
            else:
              return add_foods(user)

      elif user_choice == '4':
        return logged_into_the_system(user)
      
      else:
        print("More food options are coming!")
        continue
    

  



def your_foods(user):
  #the_users_foods = load_the_food(user)
  stuff = foods_inputed_by_user()
  users = load_the_users()
  print(f"Hey {user}!")
  print("==============================================")
  print("What's being shoved inside your stomach today?")
  print("==============================================")
  users[user].pop("password")
  users[user].pop("user_status")
  users[user].pop("user_points")
  users[user].pop("flags")

  for item in users[user].items():
    print(item[0]+ ":", ", ".join(item[1]))

  print()
  print(f"1: ADD MORE STUFF?")
  print((f"2: CHECK FOODS OFF?"))
  print("press 3 to return to front page")
  k = input("")

  if k == '1':
    return add_foods(user)
  if k == '2':
    print()
    print("WHICH?")
    print("1. FOODS: ")
    print("2. DRINKS: ")
    print("3. SNACKS: ")
    print()
    choice_1 = input("CHOICE: ")
    if choice_1  == '1':
      return types_of_foods(user, 'foods',users[user]['foods'])
    elif choice_1 == '2':
      return types_of_foods(user, 'drinks',users[user]['drinks'])
    elif choice_1 == '3':
      return types_of_foods(user, 'snacks',users[user]['snacks'])



  
  elif k == '3':
    return logged_into_the_system(user)


def types_of_foods(user, type, type_of_food):
  print(type)
  #global USER_POINTS
  users = load_the_users()
  print(f"Hey there {user}")
  while True:
    print(type_of_food)
    print("================")
    print("CHECK OFF FOODS:")
    print("================")
    print("Which of these are you planning to get rip off?")
    print()
    print(": [test]\n".join(type_of_food))
    print()
    h = input("CHOICE (type 1 to exit): ")

    if h in users[user][type]:
      print(h)
      type_of_food.remove(h)
      users[user][type].pop()
      users[user]['user_points'] += 1 if type_of_food == 'snacks' else 2

      #users[user]["user_points"] = USER_POINTS
      #save_the_user(user)
      
    elif h == '1':
      return your_foods(user)
  
    save_the_user(users)


    if len(type_of_food) == 0:
      print("Seems there's nothing to react with, add foods?")
      l = input("")
      if l == '1':
        return add_foods(user)
      else:
        return types_of_foods(user, type_of_food)




def credits(user):
  users = load_the_users()
  print("THIS PROGRAMS CREATOR:")
  print("JULIUS CYLIEN, IN HIS SENIOR YEAR IN HIGH SCHOOL.")
  time.sleep(2)
  print("PROGRAM FIRST BEGIN DEVLOPMENT IN DECEMBER 6th, 2025")
  #print("COMPLETED IN ...")
  print("COMPLETED FUNCTIONAL MVP IN DECEMBER 9th, 2025 AT 9:10 PM")
  time.sleep(3)
  while True:
    print("press 1 to return to home page.")
    user_text = input()
    if user_text == '1' and user not in users:
      return main()
    elif user_text == '1' and user in users:
      return logged_into_the_system(user)
    else:
      continue
    
    


def main():
  #data = load_the_food(), load_the_users()

  while True:
    print("=====================")
    print("Welcome to Wasteless!")
    print("=====================")
    print()
    print("1: Sign up")
    print("2: Log in")
    print("3: credits")
    print("4: LEADERBOARD, NOT MADE YET!!!!!!")
    print("5: THE SHOP, NOT MADE YET!!!!!!")
    print("6: EXIT")


  
    user = input("TYPE: ")
    if user == "1":
      return user_signUP()
    elif user == "2":
      return user_login()
    elif user == '3':
      return credits(user)
    elif user == '4':
      return ranking_of_the_users(user)
    
    elif user == '5':
      #return mini_shop()
      print("come back soon")
    elif user == '6':
      print("see ya!")
      break
  



def logged_into_the_system(user):
  #data = load_the_food(), load_the_users()
  users = load_the_users()
  ONLINE = 'online'
  OFFLINE = 'offline'
  if user in users:
    users[user]['user_status'] = ONLINE
  else:
    users[user]['user_status'] = OFFLINE

  while True:
    print("=====================")
    print(f"Hello {user}! What's the deal today?")
    print("=====================")
    print()
    print("1: YOUR FOODS")
    print("2: credits")
    print("3: LEADERBOARD, NOT MADE YET!!!!!!")
    print("4: THE SHOP, NOT MADE YET!!!!!!")
    print("5: Log out")
    print("6: EXIT")


  
    user_text = input("TYPE: ")
    if user_text == "1":
      return your_foods(user)
    elif user_text == '2':
      return credits(user)
    elif user_text == '3':
      #return ranking_of_the_users(user)
      return ranking_of_the_users(user)
    elif user_text == '4':
      #return mini_shop(user)
      print("Come back soon")
    elif user_text == '5':
      return main()
    else:
      print("see ya!")
      break
  


if __name__ == "__main__":
  main()