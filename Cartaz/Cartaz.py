from PIL import Image, ImageDraw, ImageFont, ImageFilter
from Config import get_Config
import os

CPU_COUNT = os.cpu_count()


# ######################### PATH #########################  
def get_Font(nome_Fonte, tamanho_Fonte):
    font_path = os.path.join(get_Path(1), 'Data', 'Fonts', f'{nome_Fonte}.ttf')
    return ImageFont.truetype(font_path, int(tamanho_Fonte))

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
    text = text.resize(
            (
                text.width, 
                int(info['Height'])
            )
        )
    if int(info['Width']) < text.width:
        text = text.resize(
            (
                int(info['Width']), 
                text.height
            )
        )
    return text, int(info["Top_Position"])

def get_Cartaz(cartaz_Type, text, value):
    os.system('cls')
    config = get_Config(cartaz_Type)
    base_Cartaz = get_Base_Cartaz(cartaz_Type)
    
    # ########### Logo ###########
    logo, logo_Pos = get_Adjusted_Logo(config['Logo'])
    base_Cartaz.paste(logo, logo_Pos, logo)
    
    # ########### Texto superior ###########
    first_Text, first_Text_Pos = get_Adjusted_Text(config['First_Text'], text[0])
    base_Cartaz.paste(first_Text, ( int(base_Cartaz.width/2  - first_Text.width/2), first_Text_Pos), first_Text)

    
    # ########### Texto do meio ###########
    middle_Text, middle_Text_Pos = get_Adjusted_Text(config['Middle_Text'], text[1])
    base_Cartaz.paste(middle_Text, ( int(base_Cartaz.width/2  - middle_Text.width/2), middle_Text_Pos), middle_Text)
    
    # ########### Texto inferior ###########
    if len(text) > 2:
        last_Text, last_Text_Pos = get_Adjusted_Text(config['Last_Text'], text[2])
        base_Cartaz.paste(last_Text, ( int(base_Cartaz.width/2  - last_Text.width/2), last_Text_Pos), last_Text)
    
    

    base_Cartaz.show()
    # return cartaz
    
    return 