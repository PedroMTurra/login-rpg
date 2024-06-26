from src.services.actions.player_actions import Player_actions
import os
from time import sleep
from src.services.json_manip import JsonManip

def player_choices(p_actions: Player_actions, json_manip: JsonManip, json_path: str) -> bool:
    res = input(f"[1] Attack\n[2] Heal\n[3] Defend\n[4] Rest\n[5] Save and Exit\n-> ")
        
    if res == "1":
        p_actions.player_info["monster_hp"], p_actions.player_info["mana"] = p_actions.attack()
        print("You attacked the monster!")
        sleep(2)
    
    elif res == "2":
        p_actions.player_info["hp"] = p_actions.heal()
        print("You healed yourself!")
        sleep(2)
        return True
    
    elif res == "3":
        print("You defended yourself!")
        sleep(2)
        return True
        
    elif res == "4":
        p_actions.player_info["mana"] = p_actions.rest()
        print("You recovered some mana!")
        sleep(2)
        
    elif res == "5":
        player_dict = p_actions.player_info
        
        os.system("clear")
        print("Saving...")
        sleep(2)
        json_manip.write_in_json(player_dict, json_path)
        os.system("clear")
        print("Saved!")
        sleep(2)
        exit()
        
    return False