from src.services.json_manip import Json_manip
from src.services.path_exists import *

def register(db_path: str):
    while True:
        
        user = input("Username -> ")
        
        if path_exists(db_path, user):
            os.system("clear")
            print("User already exists")
            continue
        
        password = input("Password -> ")
        game_class = input("Class: [1] Warrior [2] Mage -> ")