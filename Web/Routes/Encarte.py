from flask import Blueprint, render_template
from Encarte.Encarte import get_Encarte

encarte_bp = Blueprint('encarte', __name__, url_prefix='/Encarte', template_folder='../Templates')

@encarte_bp.route('/', methods=['GET'])
def tela_cartaz():
    get_Encarte()
    return render_template('encarte.html', title="Encartes personalizados")
