from flask import Blueprint, render_template


encarte_bp = Blueprint('encarte', __name__, url_prefix='/Encarte', template_folder='../Templates')

@encarte_bp.route('/', methods=['GET'])
def tela_cartaz():
    return render_template('encarte.html', title="Encartes personalizados")
