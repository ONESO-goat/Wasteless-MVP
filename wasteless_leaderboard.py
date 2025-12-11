#from logged_into_system import logged_into_the_system
#from uts import load_the_users
#from uts import load_the_users, save_the_user
from logged_into_system import logged_into_the_system
from uts import load_the_users, save_the_user
import json



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

    for rank, (userr, data) in enumerate(sorted(users.items(), key=lambda x: x[1]["user_points"],reverse=True),1):
        print(f"{rank}: {userr}  {data['user_points']}")
       
# I WANT to pprint out the users, only the top 5 on the leaderboard.
    

    print()
    print("GO BACK (1)")
    r = input("")
    if r == '1' and user == 'Guest':
      from wasteless_main import main
      return main()
    elif r == '1' and user in users:
      return logged_into_the_system(user)
    
      # if users waste more food, they get a low rank


def mini_shop(user): # Prices vary on your ranking. 
  ...