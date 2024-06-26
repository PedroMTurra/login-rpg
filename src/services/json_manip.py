import json

class Json_manip:
    
    def get_json_info(json_path: str) -> dict:
        
        with open(json_path) as file:
            info = json.load(file)
            file.close()
            
        return info