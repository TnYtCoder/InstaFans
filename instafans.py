import os, sys, requests, time, instagrapi
from colorama import Fore
from instagrapi import Client
from datetime import datetime

def save_attempt(user_input):
    timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open("attempts.txt", "a") as file:
        file.write(f"'{user_input}' || date: {timestamp}\n")

# By TnYtCoder (GitHub)
# Instagrapi Used !!

time.sleep(1)
os.system('clear')
time.sleep(1)

class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

def typewriter(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

def banner():
	logo = '''
\033[92m  .__                   __             _____
  |__|  ____    _______/  |_ _____   _/ ____\_____     ____    ______
  |  | /    \  /  ___/\   __||__  \  \   __\ \__  \   /    \  /  ___/
  |  ||   |  \ \___ \  |  |   / __ \_ |  |    / __ \_|   |  \ \___ |
  |__||___|  //____  > |__|  (____  / |__|   (____  /|___|  //____  >
           \/      \/             \/              \/      \/      \/
  +-----------------------------------------------------------------+
  | GitHub : https://github.com/TnYtCoder |  ~|~,_\ /|-/`   | _     |
  | A Python Script To Increase Follower  |   | || | |_\,()(|(/_|`  |
  +-----------------------------------------------------------------+

	'''
	typewriter(logo)

banner()


with open('credentials.ini', 'r') as f:
  contents = f.read()

lines = contents.splitlines()

username = lines[1]
password = lines[2]

#api
api = Client()

if __name__ == "__main__":
    user_input = username
    save_attempt(user_input)

print("\033[91mAttempting Login !! ")

try:
	api.login(username, password)
	print("\033[33mLogin Successful !\n")
except:
	print('Login Failed !?')
	print('Please Check Your Username & Password\n')
	sys.exit()

def celeb():
        try:
                user_id = api.user_id_from_username("iamduzz0909")
                followings = api.user_following(user_id)
                followings_ids = list(followings.keys())

                for u_to_follow in followings_ids:
                        try:
                                print(f"\033[36m[>] Trying To Follow Celebrity")
                                api.user_follow(u_to_follow)
                        except instagrapi.exceptions.UserNotFound:
                                print("\033[31m[>] User Not Found !")
                        except instagrapi.exceptions.PleaseWaitFewMinutes:
                                print("\n\033[31m[>] Please Try Again After Few Minute !")
                                break
        except KeyboardInterrupt:
                print("\n\033[31m[>] Keyboard Interrupt : Script Ended !")
                sys.exit()
        except instagrapi.exceptions.UserNotFound:
                print("\n\033[31m[>] User Not Found !")

def celeb_un():
        try:
                user_id = api.user_id_from_username("iamduzz0909")
                followings = api.user_following(user_id)
                followings_ids = list(followings.keys())

                for u_to_unfollow in followings_ids:
                        try:
                                print(f"\033[36m[>] Trying To Unfollow Celebrity")
                                api.user_unfollow(u_to_unfollow)
                        except instagrapi.exceptions.UserNotFound:
                                print("\033[31m[>] User Not Found !")
                        except instagrapi.exceptions.PleaseWaitFewMinutes:
                                print("\n\033[31m[>] Please Try Again After Few Minute !")
                                break
        except KeyboardInterrupt:
                print("\n\033[31m[>] Keyboard Interrupt : Script Ended !")
                sys.exit()
        except instagrapi.exceptions.UserNotFound:
                print("\n\033[31m[>] User Not Found !")

print("\033[92m[1]  Start")
print("\033[92m[2]  Remove")
print("\033[91m[3]  Exit\n")


opt = int(input("\033[36mYour Option : "))
print("\n\033[92m[+] Request Accepted\n")

if opt == 1:
	celeb()

elif opt == 2:
	celeb_un()

elif opt == 3:
	print("\n\033[36m[~] Thank You For Using !!\n")
	sys.exit()

else:
	print("Incorrect Option !!\n")
	sys.exit()

print("\n\033[36m[~] Thank You For Using !!")
