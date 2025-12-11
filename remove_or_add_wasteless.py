from uts import load_the_users, FLAGGED_USERS, save_the_user
#from logged_into_system import logged_into_the_system
import time
import random
import json
#from uts import load_the_users, save_the_user
from logged_into_system import logged_into_the_system
from uts import load_the_users, save_the_user
from datetime import timedelta, datetime



def add_foods(user):
  #food = load_the_food()
  users = load_the_users()
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
      from type_of_foods import types_of_foods
      return types_of_foods(user, 'foods',users[user]['foods'])
    elif choice_1 == '2':
      from type_of_foods import types_of_foods
      return types_of_foods(user, 'drinks',users[user]['drinks'])
    elif choice_1 == '3':
      from type_of_foods import types_of_foods
      return types_of_foods(user, 'snacks',users[user]['snacks'])



  
  elif k == '3':
    return logged_into_the_system(user)
