from src.services.path_exists import *
from src.usecases.create_user import create_user

def register(db_path: str):
    while True:
        
        user = input("Username -> ")
        
        if path_exists(db_path, user):
            os.system("clear")
            print("User already exists")
            continue
        
        password = input("Password -> ")
        
        create_user(os.path.join(db_path, f"{user}.json"), user, password)
        
        os.system("clear")
        
        break