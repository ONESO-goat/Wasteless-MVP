from sign_up_log_in_wasteless import user_signUP, user_login
from uts import load_the_users, save_the_food, save_the_user, load_the_food, FLAGGED_USERS
from wasteless_leaderboard import ranking_of_the_users
from remove_or_add_wasteless import your_foods, add_foods
from logged_into_system import logged_into_the_system
from credits_wasteless import credits_julius
import time
import random
import json
from datetime import timedelta, datetime

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
      return credits_julius(user)
    elif user == '4':
      return ranking_of_the_users(user)
    
    elif user == '5':
      #return mini_shop()
      print("come back soon")
    elif user == '6':
      print("see ya!")
      break
  


if __name__ == "__main__":
  main()
