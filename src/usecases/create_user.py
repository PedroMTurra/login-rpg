from random import randint
from src.services.json_manip import JsonManip

def create_user(json_manip: JsonManip, json_path: str, user: str, password: str):
    res = input("Class: [1] Warrior [2] Mage -> ")
        
    if res == "1":
        game_class = "warrior"
        hp = randint(12, 15)
        mana = randint(5,8)
    elif res == "2":
        game_class = "mage"
        hp = randint(8, 12)
        mana = randint (10, 14)
    
    model = {
        "username": user,
        "password": password,
        "class": game_class,
        "hp": hp,
        "mana": mana,
        "round": 1,
        "monster_hp": 20
    }
    
    json_manip.write_in_json(model, json_path)