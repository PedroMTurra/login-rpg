from src.services.path_exists import *
from src.usecases.create_user import create_user
from src.services.json_manip import JsonManip

def register(db_path: str, json_manip: JsonManip):
    while True:
        
        user = input("Username -> ")
        
        if path_exists(db_path, user):
            os.system("clear")
            print("User already exists")
            continue
        
        password = input("Password -> ")
        
        create_user(json_manip, os.path.join(db_path, f"{user}.json"), user, password)
        
        os.system("clear")
        
        break