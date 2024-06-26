from src.services.path_exists import *
from src.services.json_manip import Json_manip

json_manip = Json_manip

def login(db_path: str) -> dict:
    while True:
    
        user = input("Username -> ")
                
        if not path_exists(db_path, user):
            os.system("clear")
            print("Could not find user")
            continue
        
        info = json_manip.get_json_info(os.path.join(db_path, f"{user}.json"))
        
        os.system("clear")
        
        password = input("Password -> ")
        
        if password != info["password"]:
            os.system("clear")
            print("Incorrect password")
            continue
        
        os.system("clear")
        
        return info