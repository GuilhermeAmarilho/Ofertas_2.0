from flask import Blueprint, render_template, request, jsonify
from Encarte.Encarte import get_Encarte
from Storage.Lista_Promo import getListItems
from Image_Location.Find_In_Files import find_File
from Image_Location.Find_In_Web import find_Web

encarte_bp = Blueprint('encarte', __name__, url_prefix='/Encarte', template_folder='../Templates')

@encarte_bp.route('/', methods=['GET'])
def tela_cartaz():
    get_Encarte()
    items = getListItems()
    return render_template('encarte.html', title="Encartes personalizados", items=items)

@encarte_bp.route('/QueryImg', methods=['GET', 'POST'])
def QueryImg():
    data = request.get_json(silent=True) or {}
    nome = data.get("nome")
    result = find_File(nome)
    return jsonify(result)

@encarte_bp.route('/QueryGoogle', methods=['GET', 'POST'])
def QueryGoogle():
    data = request.get_json(silent=True) or {}
    nome = data.get("nome")
    result = find_Web(nome)
    return jsonify(result)