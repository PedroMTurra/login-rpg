from src.usecases.player_choices import *

def game(p_actions: Player_actions, json_manip: JsonManip, json_path: str):
    # dar um os.system("clear")
    # inicio do round, printar todas as informações do player e do monstro
    # dar as opções de escolha do player, incluindo salvar e sair
    # fazer todas as condicionais, considerando que o monstro pode defender o ataque do player
    while True:
    
        player_class = p_actions.player_info["class"]
        player_hp = p_actions.player_info["hp"]
        player_mana = p_actions.player_info["mana"]
        player_round = p_actions.player_info["round"]
        monster_hp = p_actions.player_info["monster_hp"]
        
        os.system("clear")
        
        print(f"Class: {player_class} | HP: {player_hp} | Mana: {player_mana} | Round: {player_round}\nMonster HP: {monster_hp}\n")
        
        choice = player_choices(p_actions, json_manip, json_path)
        
        if not choice:
            
            p_actions.player_info["hp"] -= 3
            print("The monster attacked you!")
            sleep(2)
        
        if p_actions.player_info["hp"] <= 0:
            
            print("You died!")
            
            sleep(3)
            
            exit()
        
        if p_actions.player_info["monster_hp"] <= 0:
            res = input("Monster defeated! Want to continue? [1] YES [2] NO -> ")
            
            if res == "1":
                os.system("clear")
                print("Continuing to next round...")
                sleep(2)
                p_actions.player_info["round"] += 1
                
                p_actions.player_info["monster_hp"] = 10 + 10 * p_actions.player_info["round"]
                
                continue
                
            elif res == "2":
                os.system("clear")
                print("Saving...")
                sleep(2)
                
                p_actions.player_info["round"] += 1
                
                p_actions.player_info["monster_hp"] = 10 + 10 * p_actions.player_info["round"]
                
                json_manip.write_in_json(p_actions.player_info, json_path)
                os.system("clear")
                print("Saved!")
                exit()