
#from uts import load_the_users, save_the_user
#from uts import load_the_users, save_the_user
from logged_into_system import logged_into_the_system
from uts import load_the_users, save_the_user
import json

from datetime import timedelta, datetime


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
      from remove_or_add_wasteless import your_foods
      return your_foods(user)
  
    save_the_user(users)


    if len(type_of_food) == 0:
      print("Seems there's nothing to react with, add foods?")
      l = input("")
      if l == '1':
        from remove_or_add_wasteless import add_foods
        return add_foods(user)
      else:
        return types_of_foods(user, type_of_food)