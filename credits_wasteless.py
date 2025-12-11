#from uts import load_the_users, save_the_user
from logged_into_system import logged_into_the_system
from uts import load_the_users, save_the_user


import time
import random
from datetime import timedelta, datetime



def credits_julius(user):
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
      from wasteless_main import main
      return main()
    elif user_text == '1' and user in users:
      return logged_into_the_system(user)
    else:
      continue