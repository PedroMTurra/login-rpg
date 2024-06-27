import json

class JsonManip:
    
    def get_json_info(json_path: str) -> dict:
        
        with open(json_path) as file:
            info = json.load(file)
            file.close()
            
        return info
    
    def write_in_json(self, player_info: dict, json_path: str) -> None:
        
        with open(json_path, "w") as file:
            
            file.write(json.dumps(player_info, indent=3))
            file.close()