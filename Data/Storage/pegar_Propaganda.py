import os
def tamanho_do_vetor(vetor):
    total = 0
    for item in vetor:
        total += len(item)
    return total
def organizando_linha_vertical(item):
    subItens = item.split(' ')
    subItens.pop()
    resultItem = []
    if (len(subItens) < 4):
        i = 0 
        while i < 3:
            try:
                resultItem.append(subItens[i])
            except:
                resultItem.append('')
            i+=1
    else:
        i=0
        while (i < 3):
            texto_resultado = ''
            while (len(texto_resultado) < tamanho_do_vetor(subItens)/1.2):
                if(len(texto_resultado) == 0):
                    texto_resultado += subItens.pop(0)
                else:
                    texto_resultado += ' ' + subItens.pop(0)
            resultItem.append(texto_resultado)
            i+=1
    return resultItem
def organizando_linha_horizontal(item):
    subItens = item.split(' ')
    subItens.pop()
    resultItem = []
    if (len(subItens) < 3):
        i = 0 
        while i < 2:
            try:
                resultItem.append(subItens[i])
            except:
                resultItem.append('')
            i+=1
    else:
        i=0
        texto_resultado = ''
        while (len(texto_resultado) < tamanho_do_vetor(subItens)/1.2):
            if(len(texto_resultado) == 0):
                texto_resultado += subItens.pop(0)
            else:
                texto_resultado += ' ' + subItens.pop(0)
        resultItem.append(texto_resultado)
        texto_resultado = ''
        for itens_do_subItens in subItens:
            if(len(texto_resultado) == 0):
                texto_resultado += itens_do_subItens
            else:
                texto_resultado += ' ' + itens_do_subItens
        resultItem.append(texto_resultado)
    return resultItem
def organizando_valor(item):
    subItens = item.split(' ')
    valor = subItens.pop()
    valor.replace(',','.')
    return valor
def pegarPropagandaCompleta():
    i = 0
    promocao_completa = []
    file_path = ((os.path.abspath(__file__)).replace('\\pegar_Propaganda.py', ''))
    with open((file_path+'\\dados_ofertas.txt'), 'r', encoding='utf8') as arquivo:
        for linha in arquivo:
            promocao_atual= []
            item = linha.strip()
            promocao_atual.append(organizando_linha_vertical(item))
            promocao_atual.append(organizando_linha_horizontal(item))
            promocao_atual.append(organizando_valor(item))
            promocao_completa.append(promocao_atual)
    return promocao_completa