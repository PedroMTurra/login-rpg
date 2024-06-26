from src.usecases.login import login

def login_and_register(db_path: str) -> dict:    
        res = input("[1] LOGIN [2] REGISTER -> ")
        
        if res == "1": 
            return login(db_path)
                    
        elif res == "2": #se escolher registrar:
            raise NotImplementedError
                #pedir usuario
                #se usuario nao existir:
                    #pedir uma senha
                    #pedir a classe
                    #criar o arquivo json com o nome do usuario
