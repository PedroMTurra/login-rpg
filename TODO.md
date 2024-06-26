LOGIN AND REGISTER SYSTEM (WIP):
- I'll make this system using a simple json file for each user, which will be located at src/users
- In each file, informations like username, password, game class, health points, etc will be stored
- To verify if a certain username already exists, I'll just make a function to see if a file with that name is already created. If it is, the program will ask for another username
- Json model for example:

    {
        "username": string,
        "password": string,
        "class": string,
        "hp": int,
        "mana": int,
        "round": int
    }

- The username and password will be used just for login purposes, and the rest of the info will be used in the actual RPG
- Players will be able to save a "checkpoint", which is just an update of the info in json files