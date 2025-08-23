from flask import Blueprint, render_template, request, jsonify
from Encarte.Encarte import get_Encarte
from Storage.Lista_Promo import getListItems


encarte_bp = Blueprint('encarte', __name__, url_prefix='/Encarte', template_folder='../Templates')

@encarte_bp.route('/', methods=['GET'])
def tela_cartaz():
    get_Encarte()
    items = getListItems()
    return render_template('encarte.html', title="Encartes personalizados", items=items)

@encarte_bp.route('/QueryImg', methods=['GET', 'POST'])
def QueryImg():
    print("\n\n\n\n\n\n\n")
    data = request.get_json(silent=True) or {}
    nome = data.get("nome")
    if not nome:
        return jsonify({"ok": False, "error": "Campo 'nome' é obrigatório."}), 400
    else:
        print([nome])
    return jsonify({
        "ok": True,
        "nome": nome,
    }), 200