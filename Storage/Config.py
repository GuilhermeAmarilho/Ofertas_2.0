import os, json

def get_Path(level = 0):
    return "\\".join(os.path.abspath(__file__).split('\\')[:(-1-level)])

def get_Config(key=None, default=None):
    path = get_Path(0) + "\\Config.json"
    try:
        with open(path, 'r', encoding='utf-8') as f:
            _json = json.load(f)
            if key == None:
                return _json
            else:
                return _json.get(key, default)
    except:
        return False

def get_Themes():
    path = "\\".join(os.path.abspath(__file__).split('\\')[:-2]) + "\\Web\\Static\\Assets\\Themes"
    pastas = [
        nome for nome in os.listdir(path) 
        if os.path.isdir(
            os.path.join(path, nome)
        ) and nome != 'Base_Para_Photoshop'
    ]
    return pastas

def update_Config(key, values):
    path = get_Path(0) + "\\Config.json"
    try:
        with open(path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        config[key] = values
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print("Erro ao salvar configuração:", e)
        return False