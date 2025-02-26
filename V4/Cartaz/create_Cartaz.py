import shutil, os, zipfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from Data.DataManagement import getConfig, getPromo

def verificar_Modelo():
    path = pegar_Path_Inicial() + '\\static\\Modelo'
    if os.path.exists(path) and os.path.isdir(path):
        return 
    else:
        os.makedirs(path)

def deletar_Modelo():
    path = pegar_Path_Inicial()+'\\static\\Modelo'
    if os.path.exists(path):
        shutil.rmtree(path)

def verificar_Encarte():
    path = pegar_Path_Inicial() + '\\static\\Temp'
    if os.path.exists(path) and os.path.isdir(path):
        return 
    else:
        os.makedirs(path)

def compactar_Arquivos():
    diretorio_para_zip = 'DataContent\\Encarte'
    arquivo_zip = getConfig['Path Salvamento']+'\\Encartes.zip'
    with zipfile.ZipFile(arquivo_zip, 'w') as zipf:
        for pasta_raiz, subdirs, arquivos in os.walk(diretorio_para_zip):
            for arquivo in arquivos:
                caminho_completo = os.path.join(pasta_raiz, arquivo)
                zipf.write(caminho_completo, os.path.relpath(caminho_completo, diretorio_para_zip))
    shutil.rmtree(pegar_Path_Inicial()+'\\DataContent\\Encarte')
    os.makedirs(pegar_Path_Inicial()+'\\DataContent\\Encarte')

def pegar_Path_Inicial():
    path = "\\".join(os.path.abspath(__file__).split('\\')[:-2])
    return path

def pegar_Path_Encarte(tipo_Encarte):
    file_path = pegar_Path_Inicial() + '\\static\\Temas\\' + getConfig()['Tema_Escolhido'] + '\\' + tipo_Encarte + '.png'
    return file_path

def pegar_Path_Salvamento():
    return getConfig()['Path_Salvamento']

def pegar_Path_Logo():
    logo_path = pegar_Path_Inicial() + '\\static\\Logo\\' + getConfig()['Logo_Escolhida'] + '.png'
    return logo_path

def pegar_Path_Balao():
    balao_path = pegar_Path_Inicial() + '\\static\\Balao\\' + getConfig()['Balao_Escolhido'] + '.png'
    return balao_path

def converter_Fator_0(valor, fator0):
    fator_0 = fator0/100 + 1
    valor = (float(valor.replace(',','.'))) * fator_0
    new_Value = f"{valor:.2f}".replace('.',',')
    return new_Value

def pegar_Fonte(nome_Fonte, tamanho_Fonte):
    font = ImageFont.truetype(
        (
            pegar_Path_Inicial() + '\\static\\Fontes\\' + nome_Fonte + '.ttf'
        ), 
        int(tamanho_Fonte)
    )
    return font

def pegar_Icone(nome, informacoes):
    file_path = pegar_Path_Inicial()
    icone_path = file_path + '\\static\\Icons\\' + nome + '.png'
    icone = Image.open(icone_path)
    icone = bordar_Imagens(icone, informacoes)
    icone = icone.resize(
        (
            int(informacoes['Tamanho_Da_Fonte']),
            int(informacoes['Tamanho_Da_Fonte'])
        )
    )
    return icone

def inserir_Fundo(cartaz):
    imagem_Branca = Image.new(
        'RGBA', 
        (cartaz.width, cartaz.height), 
        color = (255, 255, 255, 255)
    )
    imagem_Branca.paste(cartaz, (0,0), cartaz)
    return imagem_Branca

def bordar_Imagens(imagem, informacoes):
    tamanho_Da_Borda = int(informacoes['Tamanho_Da_Borda'])
    largura_Total = imagem.width + tamanho_Da_Borda*2
    Altura_Total = imagem.height + tamanho_Da_Borda*2
    sombra = imagem.copy()
    pixels = sombra.load()
    for i in range(imagem.width):
        for j in range(imagem.height):
            r, g, b, a = pixels[i, j]
            if a > 0:
                pixels[i, j] = (0, 0, 0, a)
    sombra = sombra.resize(
        (
            largura_Total,
            Altura_Total
        )
    )
    sombra.paste(imagem, (tamanho_Da_Borda, tamanho_Da_Borda), imagem)
    bbox = sombra.getbbox()
    if bbox:
        sombra = sombra.crop(bbox)
    return sombra

def inserir_Logo(cartaz, informacoes):
    logo_path = pegar_Path_Logo()
    logo = Image.open(logo_path)
    logo = bordar_Imagens(logo, informacoes)
    logo = logo.resize(
        (
            int(informacoes['Largura_Maxima']), 
            int(informacoes['Altura'])
        )
    )
    posicao = (
        int(informacoes['Distancia_Esquerda']), 
        int(informacoes['Distancia_Topo'])
    )
    cartaz.paste(logo, posicao, logo)
    return cartaz

def criar_Sombra_Para_Bordar_Textos(informacoes, texto, margem, fonte, altura_Maxima, largura_Texto, blur = 5):
    cor_Borda = (int(informacoes['Cor_Da_Borda']['R']),int(informacoes['Cor_Da_Borda']['G']),int(informacoes['Cor_Da_Borda']['B']))
    imagem = Image.new('RGBA', (largura_Texto, altura_Maxima), color = (0, 0, 0, 0))
    area_de_Trabalho = ImageDraw.Draw(imagem)
    area_de_Trabalho.text((margem-margem,margem-margem), texto, font = fonte, fill = cor_Borda) # Diagonal Superior Esquerda
    area_de_Trabalho.text((margem+margem,margem-margem), texto, font = fonte, fill = cor_Borda) # Diagonal Superior Direita
    area_de_Trabalho.text((margem+margem,margem+margem), texto, font = fonte, fill = cor_Borda) # Diagonal Inferior Direita
    area_de_Trabalho.text((margem-margem,margem+margem), texto, font = fonte, fill = cor_Borda) # Diagonal Inferior Esquerda 
    area_de_Trabalho.text((margem-margem,margem), texto, font = fonte, fill = cor_Borda) # Projeção Centro Esquerda
    area_de_Trabalho.text((margem+margem,margem), texto, font = fonte, fill = cor_Borda) # Projeção Centro Direita
    area_de_Trabalho.text((margem,margem-margem), texto, font = fonte, fill = cor_Borda) # Projeção Centro Superior
    area_de_Trabalho.text((margem,margem+margem), texto, font = fonte, fill = cor_Borda) # Projeção Centro Inferior
    bbox = imagem.getbbox()
    if bbox:
        imagem = imagem.crop(bbox)
    imagem = imagem.filter(ImageFilter.GaussianBlur(radius=blur))
    return imagem

def criar_Texto_Centralizado_Sob_A_Borda(informacoes, texto, fonte, altura_Maxima, largura_Texto):
    cor_Fonte = (int(informacoes['Cor_Da_Fonte']['R']),int(informacoes['Cor_Da_Fonte']['G']),int(informacoes['Cor_Da_Fonte']['B']))
    imagem = Image.new('RGBA', (largura_Texto, altura_Maxima), color = (0, 0, 0, 0))
    area_de_Trabalho = ImageDraw.Draw(imagem)
    area_de_Trabalho.text((0, 0), texto, font = fonte, fill = cor_Fonte)
    bbox = imagem.getbbox()
    if bbox:
        imagem = imagem.crop(bbox)
    return imagem

def bordar_Textos(texto, informacoes, blur = 5, multiplicador = 1):
    margem = int(int(informacoes['Tamanho_Da_Borda']) * multiplicador)
    fonte = pegar_Fonte(informacoes['Nome_Da_Fonte'],informacoes['Tamanho_Da_Fonte'])
    altura_Maxima = int(int(informacoes['Tamanho_Da_Fonte']) * 1.5)
    largura_Texto = len(texto) * int(informacoes['Tamanho_Da_Fonte'])
    sombra = criar_Sombra_Para_Bordar_Textos(informacoes, texto, margem, fonte, altura_Maxima, largura_Texto, blur)
    texto_Central = criar_Texto_Centralizado_Sob_A_Borda(informacoes, texto, fonte, altura_Maxima, largura_Texto)
    imagem = Image.new('RGBA', (sombra.width, sombra.height), color = (0, 0, 0, 0))
    imagem.paste(sombra, (0,0), sombra)
    imagem.paste(texto_Central, (margem, margem), texto_Central)
    bbox = imagem.getbbox()
    if bbox:
        imagem = imagem.crop(bbox)
    return imagem
    
def inserir_Texto(cartaz, texto, informacoes):
    texto = bordar_Textos(texto, informacoes)
    if(texto.width > int(informacoes['Largura_Maxima'])):
        dimensoes = (
            int(informacoes['Largura_Maxima']), 
            int(informacoes['Altura'])
        )
    else:
        dimensoes = (
            texto.width,
            int(informacoes['Altura'])
        )
    texto = texto.resize(dimensoes)
    coordenadas = (
        int( ( cartaz.width - texto.width ) / 2 ),
        int(informacoes['Distancia_Topo'])
        )
    cartaz.paste(texto, coordenadas, texto)
    return cartaz

def inserir_Balao(cartaz, informacoes):
    balao_path = pegar_Path_Balao()
    balao = Image.open(balao_path)
    balao = balao.resize(
        (
            int(informacoes['Largura']), 
            int(informacoes['Altura'])
        )
    )
    balao = bordar_Imagens(balao, informacoes)
    posicao = (
        int((cartaz.width - balao.width)/2), 
        int(informacoes['Distancia_Topo'])
    )
    cartaz.paste(balao, posicao, balao)
    return cartaz    

def inserir_preco(cartaz, valor, informacoes):
    preco_Grande = valor.split(',')[0]
    preco_Pequeno = ',' + valor.split(',')[1]
    preco_Grande = bordar_Textos(preco_Grande, informacoes, 2)
    preco_Pequeno = bordar_Textos(preco_Pequeno, informacoes, 5, 2)
    preco_Pequeno = preco_Pequeno.resize(
        (
            int( preco_Pequeno.width / int(informacoes['Proporcao_Grande/Pequena'])), 
            int( preco_Pequeno.height / int(informacoes['Proporcao_Grande/Pequena']))
        )
    )
    largura = preco_Grande.width + preco_Pequeno.width
    altura = preco_Grande.height
    preco_Completo = Image.new(
        'RGBA', 
        (largura, int(altura * 1.1)), 
        color = (0, 0, 0, 0)
    )
    preco_Completo.paste(preco_Grande, (0, int(altura*0.05)), preco_Grande)
    preco_Completo.paste(preco_Pequeno, (preco_Grande.width, int(altura*0.05)), preco_Pequeno)
    dimensoes = (
        int(informacoes['Largura']),
        int(informacoes['Altura'])
    )
    preco_Completo = preco_Completo.resize(dimensoes)
    posicao = (
        int((cartaz.width - preco_Completo.width)/2),
        int(informacoes['Distancia_Topo'])
    )
    cartaz.paste(preco_Completo, posicao, preco_Completo)
    return cartaz

def inserir_RS(cartaz, informacoes):
    fonte = pegar_Fonte(informacoes['Nome_Da_Fonte'], informacoes['Tamanho_Da_Fonte'])
    texto = informacoes['Texto']
    rs = bordar_Textos(texto, informacoes)
    rs = rs.resize(
        (
            int(informacoes['Largura']), 
            int(informacoes['Altura'])
        )
    )
    coordenadas = (
        int(informacoes['Distancia_Esquerda']),
        cartaz.height - int(informacoes['Distancia_Baixo'])
        )
    cartaz.paste(rs, coordenadas, rs)
    return cartaz

def inserir_Localizacao(cartaz, informacoes):
    texto_Superior = bordar_Textos(informacoes['Texto_1'], informacoes)
    texto_Inferior = bordar_Textos(informacoes['Texto_2'], informacoes)
    altura_Localizacao = texto_Superior.height + texto_Inferior.height 
    if(texto_Superior.width >= texto_Inferior.width):
        largura_Localizacao = texto_Superior.width
    else:
        largura_Localizacao = texto_Inferior.width
    imagem_Localizacao = Image.new(
        'RGBA', 
        (largura_Localizacao, altura_Localizacao), 
        color = (255, 255, 255, 0)
    )
    imagem_Localizacao.paste(texto_Superior, (0, 0), texto_Superior)
    imagem_Localizacao.paste(texto_Inferior, (0,texto_Superior.height), texto_Inferior)
    dimensoes = (
        int(informacoes['Largura']),
        int(informacoes['Altura'])
    )
    imagem_Localizacao = imagem_Localizacao.resize(dimensoes)
    posicao = (
        int(informacoes['Distancia_Esquerda']),
        (cartaz.height - int(informacoes['Distancia_Baixo']))
    )
    cartaz.paste(imagem_Localizacao, posicao, imagem_Localizacao)
    return cartaz

def inserir_Texto_Nas_Redes_Sociais(tipo, texto, informacoes):
    texto = bordar_Textos(texto, informacoes, 2)
    icon_Rede_social = pegar_Icone(tipo, informacoes)
    imagem = Image.new(
        'RGBA', 
        (icon_Rede_social.width + texto.width, icon_Rede_social.height), 
        color = (255, 255, 255, 0)
    )
    imagem.paste(icon_Rede_social, (0,0), icon_Rede_social)
    imagem.paste(
        texto, 
        (
            icon_Rede_social.width, int((imagem.height - texto.height)/2)
        ),
        texto
    )
    return imagem

def inserir_Redes_Sociais(cartaz, informacoes):
    facebook = inserir_Texto_Nas_Redes_Sociais('Facebook', informacoes['Facebook'], informacoes)
    instagram = inserir_Texto_Nas_Redes_Sociais('Instagram', informacoes['Instagram'], informacoes)
    whatsapp = inserir_Texto_Nas_Redes_Sociais('Whatsapp', informacoes['Whatsapp'], informacoes)
    imagem = Image.new(
        'RGBA', 
        (
            max(facebook.width, instagram.width, whatsapp.width), 
            facebook.height + instagram.height + whatsapp.height    
        ), 
        color = (255, 255, 255, 0)
    )
    imagem.paste(facebook, (0, 0), facebook)
    imagem.paste(instagram, (0, facebook.height), instagram)
    imagem.paste(whatsapp, (0, facebook.height + instagram.height), whatsapp)
    dimensoes = (
        int(informacoes['Largura']),
        int(informacoes['Altura'])
    )
    imagem = imagem.resize(dimensoes)
    posicao = (
        cartaz.width - (int(informacoes['Distancia_Direita']) + imagem.width),
        (cartaz.height - int(informacoes['Distancia_Baixo']))
    )
    cartaz.paste(imagem, posicao, imagem)
    return cartaz

def criar_Cartaz_Vertical(dados, vetor_palavras, valor, contador = 0, modelo_Base = False):
    path_img = pegar_Path_Encarte('Vertical')
    cartaz = Image.open(path_img)
    cartaz = inserir_Fundo(cartaz)
    cartaz = inserir_Logo(cartaz, dados['Logo'])
    cartaz = inserir_Texto(cartaz, vetor_palavras[0], dados['Texto_Superior'])
    cartaz = inserir_Texto(cartaz, vetor_palavras[1], dados['Texto_Medio'])
    if (vetor_palavras[2] != ''):
        cartaz = inserir_Texto(cartaz, vetor_palavras[2], dados['Texto_Inferior'])
    inserir_Balao(cartaz, dados['Balao'])
    cartaz = inserir_preco(cartaz, valor, dados['Preco'])
    cartaz = inserir_RS(cartaz, dados['R$'])
    cartaz = inserir_Localizacao(cartaz, dados['Localizacao'])
    cartaz = inserir_Redes_Sociais(cartaz, dados['Redes_Sociais'])
    if modelo_Base:
        cartaz.save(pegar_Path_Inicial() + '\\static\\Temp\\Vertical' + '-' + str(contador) + '.png')
    else:
        cartaz.save(pegar_Path_Inicial() + '\\static\\Modelo\\Vertical.png')

def criar_Cartaz_Story(dados, vetor_palavras, valor, contador = 0, modelo_Base = False):
    path_img = pegar_Path_Encarte('Story')
    cartaz = Image.open(path_img)
    cartaz = inserir_Fundo(cartaz)
    cartaz = inserir_Logo(cartaz, dados['Logo'])
    cartaz = inserir_Texto(cartaz, vetor_palavras[0], dados['Texto_Superior'])
    cartaz = inserir_Texto(cartaz, vetor_palavras[1], dados['Texto_Medio'])
    if (vetor_palavras[2] != ''):
        cartaz = inserir_Texto(cartaz, vetor_palavras[2], dados['Texto_Inferior'])
    inserir_Balao(cartaz, dados['Balao'])
    cartaz = inserir_preco(cartaz, valor, dados['Preco'])
    cartaz = inserir_RS(cartaz, dados['R$'])
    cartaz = inserir_Localizacao(cartaz, dados['Localizacao'])
    cartaz = inserir_Redes_Sociais(cartaz, dados['Redes_Sociais'])
    if modelo_Base:
        cartaz.save(pegar_Path_Inicial() + '\\static\\Temp\\Story' + '-' + str(contador) + '.png')
    else:
        cartaz.save(pegar_Path_Inicial() + '\\static\\Modelo\\Story.png')

def criar_Cartaz_Horizontal(dados, vetor_palavras, valor, contador = 0, modelo_Base = False):
    path_img = pegar_Path_Encarte('Horizontal')
    cartaz = Image.open(path_img)
    cartaz = inserir_Fundo(cartaz)
    cartaz = inserir_Logo(cartaz, dados['Logo'])
    cartaz = inserir_Texto(cartaz, vetor_palavras[0], dados['Texto_Superior'])
    if (vetor_palavras[1] != '') :
        cartaz = inserir_Texto(cartaz, vetor_palavras[1], dados['Texto_Medio'])
    inserir_Balao(cartaz, dados['Balao'])
    cartaz = inserir_preco(cartaz, valor, dados['Preco'])
    cartaz = inserir_RS(cartaz, dados['R$'])
    cartaz = inserir_Localizacao(cartaz, dados['Localizacao'])
    cartaz = inserir_Redes_Sociais(cartaz, dados['Redes_Sociais'])
    if modelo_Base:
        cartaz.save(pegar_Path_Inicial() + '\\static\\Temp\\Horizontal' + '-' + str(contador) + '.png')
    else:
        cartaz.save(pegar_Path_Inicial() + '\\static\\Modelo\\Horizontal.png')

def criar_Cartaz_Feed(dados, vetor_palavras, valor, contador = 0, modelo_Base = False):
    path_img = pegar_Path_Encarte('Feed')
    cartaz = Image.open(path_img)
    cartaz = inserir_Fundo(cartaz)
    cartaz = inserir_Logo(cartaz, dados['Logo'])
    cartaz = inserir_Texto(cartaz, vetor_palavras[0], dados['Texto_Superior'])
    if (vetor_palavras[1] != '') :
        cartaz = inserir_Texto(cartaz, vetor_palavras[1], dados['Texto_Medio'])
    inserir_Balao(cartaz, dados['Balao'])
    cartaz = inserir_preco(cartaz, valor, dados['Preco'])
    cartaz = inserir_RS(cartaz, dados['R$'])
    cartaz = inserir_Localizacao(cartaz, dados['Localizacao'])
    cartaz = inserir_Redes_Sociais(cartaz, dados['Redes_Sociais'])
    if modelo_Base:
        cartaz.save(pegar_Path_Inicial() + '\\static\\Temp\\Feed' + '-' + str(contador) + '.png')
    else:
        cartaz.save(pegar_Path_Inicial() + '\\static\\Modelo\\Feed.png')

def criar_Cartaz_Horizontal_Fator_0(dados, vetor_palavras, valor, fator0, i = 0):
    valor = converter_Fator_0(valor, fator0)
    path_img = pegar_Path_Encarte('Horizontal')
    cartaz = Image.open(path_img)
    cartaz = inserir_Fundo(cartaz)
    cartaz = inserir_Logo(cartaz, dados['Logo'])
    cartaz = inserir_Texto(cartaz, vetor_palavras[0], dados['Texto_Superior'])
    if (vetor_palavras[1] != '') :
        cartaz = inserir_Texto(cartaz, vetor_palavras[1], dados['Texto_Medio'])
    # inserir_Balao(cartaz, dados['Balao'])
    cartaz = inserir_preco(cartaz, valor, dados['Preco'])
    cartaz = inserir_RS(cartaz, dados['R$'])
    cartaz = inserir_Localizacao(cartaz, dados['Localizacao'])
    cartaz = inserir_Redes_Sociais(cartaz, dados['Redes_Sociais'])
    cartaz.save(pegar_Path_Inicial() + '\\DataContent\\Encarte\\Fator0' + '-' + str(i) + '.png')
    return cartaz

def criar_Modelo():
    deletar_Modelo()
    verificar_Modelo()
    config = getConfig()
    item = [['TEXTO TEXTO TEXTO', 'TEXTO TEXTO', 'TEXTO'], ['TEXTO TEXTO TEXTO', 'TEXTO TEXTO'], '99,99']
    criar_Cartaz_Vertical(config['Posicoes']['Vertical'], item[0], item[2])
    criar_Cartaz_Story(config['Posicoes']['Story'], item[0], item[2])
    criar_Cartaz_Feed(config['Posicoes']['Feed'], item[1], item[2])
    criar_Cartaz_Horizontal(config['Posicoes']['Horizontal'], item[1], item[2])

def criar_Cartaz():
    config = getConfig()
    item = [['TEXTO TEXTO TEXTO','TEXTO TEXTO','TEXTO'],['TEXTO TEXTO TEXTO','TEXTO TEXTO'],'99,99']
    criar_Cartaz_Vertical(config['Posicoes']['Vertical'], item[0], item[2])