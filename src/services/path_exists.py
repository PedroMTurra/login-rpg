import os

def path_exists(users_db_path: str, username: str):
    return os.path.exists(os.path.join(users_db_path, f"{username}.json"))