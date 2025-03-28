from PIL import Image, ImageDraw, ImageFont, ImageFilter
from Config import get_Config
import os

CPU_COUNT = os.cpu_count()


# ######################### PATH #########################  
def get_Font(nome_Fonte, tamanho_Fonte):
    font = ImageFont.truetype(
        (
            get_Path(1) + '\\Data\\Fonts\\' + nome_Fonte + '.ttf'
        ), 
        int(tamanho_Fonte)
    )
    return font

def get_Path(level = 0):
    return "\\".join(os.path.abspath(__file__).split('\\')[:(-1-level)])

def get_Base_Cartaz(modelo):
    path = get_Path(1) + '\\Data\\Themes\\' + get_Config("Theme") + "\\" + modelo + ".png"
    return Image.open(path)

def get_Logo_Path():
    logo = get_Config("Logo")
    path = get_Path(1) + '\\Data\\Logo\\' + logo + ".png"
    return path

# ######################### Ajustes de imagens #########################

def get_Adjusted_Logo(info):
    logo = Image.open(get_Logo_Path())
    original_Width, original_Height = logo.size
    width = int(info['Width'])
    fator = width / original_Width
    height = int(original_Height * fator)
    logo = logo.resize(
        (
            width, 
            height
        )
    )
    return logo, (int(info["Left_Position"]), int(info["Top_Position"]))

def get_Adjusted_Text(info, string):
    font = get_Font(info['Font_Name'], info['Font_Size'])
    font_Color = (int(info['Font_Color']['R']), int(info['Font_Color']['G']), int(info['Font_Color']['B']))
    text_Size = len(string) * int(info['Font_Size'])
    altura_Maxima = int(int(info['Font_Size']) * 1.2)
    text = Image.new('RGBA', (text_Size, altura_Maxima), color = (0, 0, 0, 0))
    area_de_Trabalho = ImageDraw.Draw(text)
    area_de_Trabalho.text((0, 0), string, font = font, fill = font_Color)
    bbox = text.getbbox()
    if bbox:
        text = text.crop(bbox)
    width = int(info['Width'])
    fator = width / text.width
    height = int(text.height * fator)
    text = text.resize(
        (
            width, 
            height
        )
    )
    return text, int(info["Top_Position"])

def get_Cartaz(type, text, value):
    os.system('cls')
    config = get_Config(type)
    base_Cartaz = get_Base_Cartaz(type)
    
    # Funções a chamar
    logo, logo_Pos = get_Adjusted_Logo(config['Logo'])
    first_Text, first_Text_Pos = get_Adjusted_Text(config['First_Text'], text[0])
    middle_Text, middle_Text_Pos = get_Adjusted_Text(config['Middle_Text'], text[1])

    # Adicionando  a imagem
    base_Cartaz.paste(logo, logo_Pos, logo)
    base_Cartaz.paste(first_Text, ( int(base_Cartaz.width/2  - first_Text.width/2), first_Text_Pos), first_Text)
    base_Cartaz.paste(middle_Text, ( int(base_Cartaz.width/2  - middle_Text.width/2), middle_Text_Pos), middle_Text)
    base_Cartaz.show()
    # return cartaz
    
    return 