import os
from .dados import pegar_Dados

def pegar_Path_Inicial():
    return os.path.abspath(__file__)[
        :
        (os.path.abspath(__file__)).lower().rfind('gerador_de_ofertas') 
        + 
        len('gerador_De_Ofertas')
    ]
def pegar_Path_Encarte(tipo_Encarte):
    tema_Propaganda = pegar_Dados()['Tema_Escolhido']
    file_path = pegar_Path_Inicial()
    tipo_Tema = '\\DataContent\\Temas\\' + tema_Propaganda
    img_path = '\\' + tipo_Encarte + '.png'
    full_path = file_path + tipo_Tema + img_path
    return full_path
def pegar_Path_Salvamento():
    return pegar_Dados()['Path_Salvamento']
def pegar_Path_Logo():
    file_path = pegar_Path_Inicial()
    logo_path = file_path + '\\DataContent\\Logo\\' + pegar_Dados()['Logo_Escolhida'] + '.png'
    return logo_path
def pegar_Path_Balao():
    file_path = pegar_Path_Inicial()
    balao_path = file_path + '\\DataContent\\Balao\\' + pegar_Dados()['Balao_Escolhido'] + '.png'
    return balao_path