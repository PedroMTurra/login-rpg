from src.groups.login_and_register import *
from src.groups.game import *

db_path = "/home/pedro/projects/login_rpg/src/database/users"
json_manip = JsonManip()

player_info = login_and_register(db_path, json_manip)
user = player_info["username"]

json_path = os.path.join(db_path, f"{user}.json")
p_actions = Player_actions(player_info)

game(p_actions, json_manip, json_path)