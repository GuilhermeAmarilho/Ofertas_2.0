from flask import Blueprint, render_template, request
from Storage.Get_Promo import getListItems, addItem, replaceList

promocao_bp = Blueprint('promocao', __name__, url_prefix='/Promocao', template_folder='../Templates')

@promocao_bp.route('/', methods=['GET'])
def tela_cartaz():
    items = getListItems()
    return render_template('promocao.html', title="Lista de Itens", items=items)
@promocao_bp.route('/AdicionarPromocaoSimples', methods=['GET', 'POST'])
def adicionarPromocaoSimples():
    if request.method == 'POST':
        data = request.json
        nome = data.get('nome')
        valor = data.get('valor')
        print(nome, valor)
        addItem(nome, valor)
    return ""
@promocao_bp.route('/AdicionarListaDePromocao', methods=['GET', 'POST'])
def AdicionarListaDePromocao():
    if request.method == 'POST':
        data = request.json
        promocoes = data.get('dados')
        for item in promocoes:
            addItem(item[0], item[1])
    return ""

@promocao_bp.route('/RemoverItemPromocao', methods=['GET', 'POST'])
def RemoverItemPromocao():
    if request.method == 'POST':
        data = request.json
        id = data.get('id')
        if isinstance(id, int):
            items = getListItems()
            new_Items = []
            for item in items:
                if not item[3] == id:
                    new_Items.append(item)
            replaceList(new_Items)
    return ""