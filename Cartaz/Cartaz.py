from PIL import Image, ImageDraw, ImageFont
import os
from .Config_Reader import get_Config
from Storage import getListItems
from multiprocessing import Pool, cpu_count

# ######################### Caminhos corretos #########################

def get_Font(nome_Fonte, tamanho_Fonte):
    font_path = os.path.join(get_Path(1), 'Design', 'Fonts', f'{nome_Fonte}.ttf')
    return ImageFont.truetype(font_path, int(tamanho_Fonte))

def get_Path(level = 0):
    return "\\".join(os.path.abspath(__file__).split('\\')[:(-1-level)])

def get_Base_Cartaz(modelo):
    path = get_Path(1) + '\\Design\\Themes\\' + get_Config("Theme") + "\\" + modelo + ".png"
    return Image.open(path)

def get_Logo_Path():
    logo = get_Config("Logo")
    path = get_Path(1) + '\\Design\\Logo\\' + logo + ".png"
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
    altura_Maxima = int(int(info['Font_Size']) * 1.3)
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

def get_Adjusted_Price(info, price):
    price = price.split(',')
    big_Price = price[0]
    small_Price = ',' + price[1]
    big_Price = get_Adjusted_Text(info, big_Price)[0]
    small_Price = get_Adjusted_Text(info, small_Price)[0]
    small_Price = small_Price.resize(
        (
            int( small_Price.width / int(info['Ratio_Large_Small'])), 
            int( small_Price.height / int(info['Ratio_Large_Small']))
        )
    )
    full_Price = Image.new('RGBA', (big_Price.width+small_Price.width, big_Price.height), color = (0, 0, 0, 0))
    full_Price.paste(big_Price, (0, 0), big_Price)
    full_Price.paste(small_Price, (big_Price.width, 0), small_Price)
    size = (
        int(info['Width']),
        int(info['Height'])
    )
    full_Price = full_Price.resize(size)
    return full_Price, int(info["Top_Position"])

def get_Adjusted_Money(info):
    money, money_Pos_Top = get_Adjusted_Text(info, info['Text'])
    money_Pos_Left = int(info['Left_Position'])
    return money, money_Pos_Top, money_Pos_Left

def get_Adjusted_Location(info):
    first_Text = get_Adjusted_Text(info,  info['First_Text'])[0]
    last_Text = get_Adjusted_Text(info, info['Last_Text'])[0]
    gap = int(info['Gap'])
    full_Height = first_Text.height + last_Text.height + gap
    if(first_Text.width >= last_Text.width):
        full_Width = first_Text.width
    else:
        full_Width = last_Text.width
    full_Location = Image.new(
        'RGBA', 
        (full_Width, full_Height), 
        color = (255, 255, 255, 0)
    )
    full_Location.paste(first_Text, (0, 0), first_Text)
    full_Location.paste(last_Text, (0, first_Text.height + gap), last_Text)
    size = (
        int(info['Width']),
        int(info['Height'])
    )
    full_Location = full_Location.resize(size)
    return full_Location, int(info['Top_Position']), int(info['Left_Position']) 

# ######################### Criação dos cartazes #########################

def get_Cartaz(cartaz_Type, text, value):
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
        if text[2] != '':
            last_Text, last_Text_Pos = get_Adjusted_Text(config['Last_Text'], text[2])
            base_Cartaz.paste(last_Text, ( int(base_Cartaz.width/2  - last_Text.width/2), last_Text_Pos), last_Text)
    # ########### Preço ###########
    price, price_Pos = get_Adjusted_Price(config['Price'], value)
    base_Cartaz.paste(price, ( int(base_Cartaz.width/2  - price.width/2), price_Pos), price)
    # ########### Tipo Monetário ###########
    type_Money, type_Money_Pos_Top, type_Money_Pos_Left = get_Adjusted_Money(config['Money'])
    base_Cartaz.paste(type_Money, (type_Money_Pos_Left, type_Money_Pos_Top), type_Money)
    # ########### Localização ###########
    location, location_Pos_Top, location_Pos_Left = get_Adjusted_Location(config['Location'])
    base_Cartaz.paste(location, (location_Pos_Left, location_Pos_Top), location)
    # ########### Compressão ###########
    base_Cartaz = base_Cartaz.convert('RGB')
    return base_Cartaz

def _worker(args):
    type, text, value, out_path = args
    get_Cartaz(type, text, value).save(out_path)

def generate_Exemple_Items(view = False, who=None):
    item = [["COXA E SOBRECOXA", "TRADICIONAL", "Kg"], ["COXA E SOBRECOXA", "TRADICIONAL Kg"], "18,99"]
    if view == False:
        cartaz_List_Path = get_Path(0) + '\\Exemple\\'
        if  not os.path.exists(cartaz_List_Path):
            os.mkdir(cartaz_List_Path)
        tasks = []
        tasks.append(("Retrato", item[0], item[2], cartaz_List_Path+"Retrato.png"))
        tasks.append(("Paisagem", item[1], item[2], cartaz_List_Path+"Paisagem.png"))
        with Pool(processes = cpu_count()) as pool:
            pool.map(_worker, tasks)
    else:
        match who:
            case "Retrato":
                get_Cartaz("Retrato", item[0], item[2]).show()
            case "Paisagem":
                get_Cartaz("Paisagem", item[1], item[2]).show()

def generate_All_Items():
    cartaz_List_Path = get_Path(0) + '\\results\\'
    if  not os.path.exists(cartaz_List_Path):
        os.mkdir(cartaz_List_Path)
    tasks = []
    for i, item in enumerate(getListItems(), start=1):
        primeiro, segundo, valor = item[0], item[1], item[2]
        tasks.append(("Retrato", primeiro, valor, cartaz_List_Path+"Retrato "+str(i)+".png"))
        tasks.append(("Paisagem", segundo, valor, cartaz_List_Path+"Paisagem "+str(i)+".png"))
    with Pool(processes=cpu_count()) as pool:
        pool.map(_worker, tasks)