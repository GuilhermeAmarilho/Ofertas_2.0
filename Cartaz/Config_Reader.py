import json, os

_path = os.path.join(os.path.dirname(__file__), 'Data.json')
with open(_path, 'r', encoding='utf-8') as f:
    _json = json.load(f)

def get_Config(key, default=None):
    return _json.get(key, default)
