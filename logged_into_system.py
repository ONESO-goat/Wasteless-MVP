
from uts import load_the_users, save_the_user

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
      from remove_or_add_wasteless import your_foods
      return your_foods(user)
    elif user_text == '2':
      from credits_wasteless import credits_julius
      return credits_julius(user)
    elif user_text == '3':
      from wasteless_leaderboard import ranking_of_the_users
      return ranking_of_the_users(user)
    elif user_text == '4':
      #return mini_shop(user)
      print("Come back soon")
    elif user_text == '5':
      from wasteless_main import main
      return main()
    else:
      print("see ya!")
      break
  
