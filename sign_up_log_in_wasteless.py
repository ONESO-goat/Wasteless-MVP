
import time
import random
import json
#from uts import load_the_users, save_the_user
from logged_into_system import logged_into_the_system
from uts import load_the_users, save_the_user
#from datetime import timedelta, datetime
#from uts import load_the_users, save_the_user
#from remove_or_add_wasteless import add_foods
#from logged_into_system import logged_into_the_system



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
          from remove_or_add_wasteless import add_foods
          return add_foods(username_create), username_create