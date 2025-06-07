from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from Cartaz.Cartaz import generate_Exemple_Items, generate_All_Items

def getConfig():
    return "teste"
cartaz_bp = Blueprint('cartaz', __name__, url_prefix='/Cartaz', template_folder='../Templates')

@cartaz_bp.route('/', methods=['GET'])
def tela_cartaz():
    # generate_Exemple_Items()
    config = getConfig()
    return render_template('cartaz.html', title="Criação de cartazes", config=config)

# @cartaz_bp.route('/getListaDeTemas', methods=['GET', 'POST'])
# def get_lista_de_temas():
#     temas = getThemes()
#     return jsonify(temas)

# @cartaz_bp.route('/atualizarTema/<tema>', methods=['GET'])
# def atualizar_tema(tema):
#     updateConfig("Tema_Escolhido", tema)
#     return redirect(url_for('cartaz.tela_cartaz'))

# Caso queira ter outra rota no mesmo blueprint:
# @cartaz_bp.route('/outra_rota', methods=['GET'])
# def outra_função():
#     ...
