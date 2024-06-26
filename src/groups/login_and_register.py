from src.usecases.login import login
from src.usecases.register import register
import os
from time import sleep

def login_and_register(db_path: str) -> dict:    
    while True:    
        
        os.system("clear")
        
        res = input("[1] LOGIN [2] REGISTER -> ")
        
        if res == "1": 
            os.system("clear")
            info = login(db_path)
            print("Login successful!")
            sleep(3)
            return info
            
        elif res == "2": 
            os.system("clear")
            register(db_path)
            print("User created!")
            sleep(3)
            continue