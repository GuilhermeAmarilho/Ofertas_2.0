import json, os

def pegar_Dados():
    try:
        path_Inicial = os.path.abspath(__file__)[
            :
            (os.path.abspath(__file__)).lower().rfind('gerador_de_ofertas') 
            + 
            len('gerador_De_Ofertas')
        ]
        with open(path_Inicial+'\\DataContent\\Banco_De_Dados\\data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return
def salvar_Dados(data):
    try:
        path_Inicial = os.path.abspath(__file__)[
            :
            (os.path.abspath(__file__)).lower().rfind('gerador_de_ofertas') 
            + 
            len('gerador_De_Ofertas')
        ]
        with open(path_Inicial+'\\DataContent\\Banco_De_Dados\\data.json', 'w',  encoding='utf-8') as f:
            return json.dump(data, f, indent=4) 
    except:
        return