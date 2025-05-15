import os, sys, time
os.system('cls')

def tamanho_do_vetor(vetor):
    total = 0
    for item in vetor:
        total += len(item)
    return total

def organizando_Linha_vertical(linha):
    resultItem = []
    partes = linha.split(' ')[:-1]
    # Texto com no máximo 3 partes de texto
    if (len(partes) < 4):
        i = 0 
        while i < 3:
            # Caso menos que 3 itens, quebraria ao tentar acessar o dado inexistente
            try:
                resultItem.append(partes[i])
            except:
                resultItem.append('')
            i+=1
    # Caso tenha mais de 4 partes de texto
    else:
        q, r = divmod(len(partes), 3)
        grupos = []
        inicio = 0
        for i in range(3):
            tamanho = q + (1 if i < r else 0) 
            grupos.append(partes[inicio:inicio+tamanho])
            inicio += tamanho
        resultItem = [" ".join(grupo) for grupo in grupos]
    return resultItem

def organizando_Linha_horizontal(linha):
    partes = linha.split(' ')[:-1]
    if len(partes) == 1:
        return [partes[0], ""]
    ruptura = 1
    diferenca = None
    # Testa todos os pontos possíveis de quebra (entre 1 e len(partes)-1)
    for i in range(1, len(partes)):
        line1 = " ".join(partes[:i])
        line2 = " ".join(partes[i:])
        diff = abs(len(line1) - len(line2))
        if diferenca is None or diff < diferenca:
            diferenca = diff
            ruptura = i

    return [" ".join(partes[:ruptura]), " ".join(partes[ruptura:])]

def organizando_valor(linha):
    valor = linha.strip().split()[-1]
    try:
        valor = float(valor.replace(",", "."))
        return f"{valor:.2f}".replace(".", ",")
    except ValueError:
        return ""

def getListItems(init = 0):
    start = time.time()
    promocao_completa = []
    file_path = ((os.path.abspath(__file__)).replace('\\Get_Promo.py', ''))
    with open((file_path+'\\Dados_ofertas.txt'), 'r', encoding='utf8') as arquivo:
        for linha in arquivo:
            if linha.find('//') == -1 and linha != '\n':
                linha = linha.replace('\n', '')
                vetor_Item = [
                    organizando_Linha_vertical(linha),
                    organizando_Linha_horizontal(linha),
                    organizando_valor(linha)
                ]
                promocao_completa.append(vetor_Item)
    return promocao_completa
getListItems()