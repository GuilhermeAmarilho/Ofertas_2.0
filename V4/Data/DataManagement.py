import os, json
def getPath(path):
    return os.path.abspath(__file__).replace('\\DataManagement.py',path)
# =============== Lista de produtos ===============
def getPromo():
    path = getPath('\\Promotions.txt')
    file = open(file = path, mode = 'r', encoding = 'utf-8' )
    promocao = []
    for item in file.readlines():
        item = item.replace('\n', "")
        item = item.split(' ')
        valor = item.pop()
        if (len(item) >= 1) and validandoPreco(valor):
            texto = organizando_Preco(item)
            texto.append(valor)
            promocao.append(texto)
    return promocao
def organizando_Preco(item):
    if (len(item) == 1):
        return [item[0], '']
    elif (len(item) == 2):
        return item
    elif (len(item) == 3):
        return [item[0], item[1] + ' ' + item[2]]
    else:
        resultItem = []
        texto_resultado = ''
        while (len(texto_resultado) < total_De_Letras_No_Vetor(item)/1.3):
            if(len(texto_resultado) == 0):
                texto_resultado += item.pop(0)
            else:
                texto_resultado += ' ' + item.pop(0)
        resultItem.append(texto_resultado)
        texto_resultado = ''
        for itens_do_subItens in item:
            if(len(texto_resultado) == 0):
                texto_resultado += itens_do_subItens
            else:
                texto_resultado += ' ' + itens_do_subItens
        resultItem.append(texto_resultado)
        return resultItem
def total_De_Letras_No_Vetor(vetor):
    total = 0
    for item in vetor:
        total += len(item)
    return total
def validandoPreco(value):
    value = value.replace(',','.')
    try:
        float(value)
        return True
    except ValueError:
        return False
def addItem(item, valor):
    try:
        valor = valor.replace(',','.')
        valor = f"{float(valor):.2f}"
        valor = valor.replace('.',',')
        file = open(file = getPath('\\Promotions.txt'), mode = 'a', encoding = 'utf-8')
        file.write('\n'+item+' '+valor)
        file.close
        return True
    except:
        return False
def updateLista(lista):
    try:
        file = open(file = getPath('\\Promotions.txt'), mode = 'w', encoding = 'utf-8')
        file.write(lista)
        file.close
        return True
    except:
        return False
# =============== Lista de produtos ===============
def getConfig():
    path = getPath('\\Configuration.json')
    file = open(file = path, mode = 'r', encoding = 'utf-8' )
    config = json.load(file)
    return config
def updateConfig(path, value):
    config = getConfig()
    keys = path.split("/")
    if len(keys) > 1:
        for key in keys[:-1]:
            last_key = keys[-1]
            if last_key in config:
                config[last_key] = value
                print(key)
                print('oi')
    else:
        config[path] = value
    file = open(file = getPath('\\Configuration.json'), mode = 'w', encoding = 'utf-8' )
    json.dump(config, file, indent=4, ensure_ascii=False)
    file.close()
    
#  =============== Lista de imagens ===============
def getThemes():
    path = "\\".join(os.path.abspath(__file__).split('\\')[:-2]) + "\\static\\Temas"
    pastas = [
        nome for nome in os.listdir(path) 
        if os.path.isdir(
            os.path.join(path, nome)
        ) and nome != 'Base_Para_Photoshop'
    ]
    return pastas