from src.usecases.login import login
from src.usecases.register import register
import os
from time import sleep
from src.services.json_manip import JsonManip

def login_and_register(db_path: str, json_manip: JsonManip) -> dict:    
    while True:    
        
        os.system("clear")
        
        res = input("[1] LOGIN [2] REGISTER [3] EXIT -> ")
        
        if res == "1": 
            os.system("clear")
            info = login(db_path)
            print("Login successful!")
            sleep(2)
            return info
            
        elif res == "2": 
            os.system("clear")
            register(db_path, json_manip)
            print("User created!")
            sleep(2)
            continue
        
        elif res == "3":
            os.system("clear")
            print("Closing...")
            sleep(2)
            exit()