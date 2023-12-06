from surval.models import UserBoardFun
from time import sleep
from surval import JOBS
import sys
import time
import random
import os



def player_data(js_data):
    python_list = [js_data]
    return python_list

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def feature_for_job(job):
    if job == 'Trader':
        trader_features = ["Analytical skills", "Market knowledge", "Negotiation skills"]
        return trader_features
    elif job == 'Healer':
        healer_features = ["Medical knowledge", "Empathy"]
        return healer_features
    elif job == 'Warrior':
        warrior_features = ["Combat skills", "Physical strength", "Tactical thinking"]
        return warrior_features
    else:
        engineer_features = ["Technical skills", "Problem-solving", "Creativity"]
        return engineer_features
def loading_animation(duration=5):
    animation_chars = "|/-\\"
    start_time = time.time()
    
    while time.time() - start_time < duration:
        for char in animation_chars:
            sys.stdout.write('\r' + f"Loading... {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    
    sys.stdout.write('\r' + "Loading... Done!\n")
    sys.stdout.flush()
def start_game():
    UserBoardFun.info("You are registered as a player in the game", "Nieuw user")
    sleep(1)
    input() # as enter of next
    UserBoardFun.info("First of all, you will register your name in the game", "User Name")
    sleep(0.3)
    input() # as enter of next
    username = input("Enter the username : ")
    sleep(1)
    UserBoardFun.info("The system chooses a job for you at random", "\n Job")
    sleep(0.2)
    input() # as enter of next
    loading_animation(5)
    chosen_job = random.choice(JOBS)
    print(f"\nYour job are : {chosen_job}")
    UserBoardFun.info("The system selects you a random feature for your job", "\n Job feature")
    sleep(0.2)
    input() # as enter of next
    loading_animation(5)
    features = feature_for_job(chosen_job)
    chosen_feature = random.choice(features)
    print('\n Your feature are : ',chosen_feature,"\n")
    input() # as enter of next
    loading_animation(5)
    UserBoardFun.info(f"The system has been established and all problems have been resolved. Welcome, {username}", "\n System")
    sleep(1)
    input()
def user_level_board():
    print("Stamina : 0\n stron : 0\n speed : 0\n skills : 0")
    

"""
Dit code is geschrijven door "Ahmad Al Dibo" maandag 4 december 2023
Contact : 
    Email : 'ahmadaldibo288@gmail.com' of 'youtuba5478@gmail.com'



"""