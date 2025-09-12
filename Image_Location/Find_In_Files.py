import os
from unidecode import unidecode
from fuzzywuzzy import process, fuzz

def find_File(nome):
    path = "\\".join(os.path.abspath(__file__).split('\\')[:(-1)]).replace("Image_Location", "Items_Image")

    # monta a relacao: nome simplificado -> nome original
    arquivos_Bruto = os.listdir(path)
    dict_Arquivos = {}
    for arquivo in arquivos_Bruto:
        nome_simplificado = os.path.splitext(arquivo)[0].lower()
        nome_simplificado = unidecode(nome_simplificado)
        dict_Arquivos[nome_simplificado] = arquivo

    # Normaliza o nome de busca
    nome = unidecode(nome.lower())
    nome = nome.replace(' kg', '')
    nome = nome.replace(' 100g', '')
    nome = nome.replace(' und', '')
    # Tenta encontrar a palavra exata
    resultados_exatos = []
    for chave in dict_Arquivos.keys():
        palavras = chave.split()
        if nome in palavras:
            resultados_exatos.append((chave, 100))
    if resultados_exatos:
        lista_final = []
        for chave, score in resultados_exatos:
            caminho = os.path.join(path, dict_Arquivos[chave])
            lista_final.append([caminho, score])
        return lista_final
    
    # Se não encontrou exato, usa fuzzy
    chaves = list(dict_Arquivos.keys())
    result = process.extractBests(nome, chaves, scorer=fuzz.token_sort_ratio, limit=5)
    lista_final = []
    for match_nome, score in result:
        if score >= 75:
            caminho = os.path.join(path, dict_Arquivos[match_nome])
            lista_final.append([caminho, score])
    return lista_final