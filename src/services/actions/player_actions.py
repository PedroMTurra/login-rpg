from random import randint

class Player_actions:
    def __init__(self, player_info: dict):
        self.player_info = player_info
        
    def attack(self):
        
        if self.player_info["class"] == "warrior":
        
            self.player_info["monster_hp"] -= randint(3, 6)
        
        elif self.player_info["class"] == "mage":
        
            self.player_info["monster_hp"] -= randint(6, 8)
            self.player_info["mana"] -= 2
            
        return self.player_info["monster_hp"], self.player_info["mana"]
            
    def rest(self) -> dict:
        
        if not self.player_info["mana"] >= 10 + 5 * self.player_info["round"]:
            
            if self.player_info["class"] == "warrior":
                
                self.player_info["mana"] += 2
                
            elif self.player_info["class"] == "mage":
                
                self.player_info["mana"] += 3
            
            if self.player_info["mana"] > 10 + 5 * self.player_info["round"]:
                
                self.player_info["mana"] = 10 + 5 * self.player_info["round"]
                
        return self.player_info["mana"]
                
    def heal(self):
        
        if not self.player_info["hp"] >= 10 + 10 * self.player_info["round"]:
            
            self.player_info["hp"] += 3
        
        if self.player_info["hp"] > 10 + 10 * self.player_info["round"]:
            
            self.player_info["hp"] = 10 + 10 * self.player_info["round"]
            
        return self.player_info["hp"]