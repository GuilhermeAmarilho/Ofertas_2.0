from flask import Blueprint, render_template, request, jsonify, redirect, url_for
# from Cartaz.Cartaz import get_Config, generate_Exemple_Items
from Cartaz.Cartaz import generate_Exemple_Items
from Storage.Config import get_Config, get_Themes, update_Config

cartaz_bp = Blueprint('cartaz', __name__, url_prefix='/Cartaz', template_folder='../Templates')

@cartaz_bp.route('/', methods=['GET'])
def tela_cartaz():
    # generate_Exemple_Items()
    config = get_Config()
    return render_template('cartaz.html', title="Criação de cartazes", config=config)

@cartaz_bp.route('/getListaDeTemas', methods=['GET', 'POST'])
def get_lista_de_temas():
    temas = get_Themes()
    return jsonify(temas)

@cartaz_bp.route('/atualizarTema/<tema>', methods=['GET'])
def atualizar_tema(tema):
    update_Config("Theme", tema)
    return redirect(url_for('cartaz.tela_cartaz'))

# Caso queira ter outra rota no mesmo blueprint:
# @cartaz_bp.route('/outra_rota', methods=['GET'])
# def outra_função():
#     ...
