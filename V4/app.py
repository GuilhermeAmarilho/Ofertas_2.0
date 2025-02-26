from flask import Flask, render_template, request, jsonify, redirect, url_for
from Data import getPromo, addItem, updateLista, getConfig, updateConfig, getThemes
from Cartaz import criar_Modelo

app = Flask(__name__)
# =================== Tela de Inicio ===================
@app.route('/')
def hello():
    return render_template('index.html', title="Página Inicial")
# =================== Tela de cartaz ===================
@app.route('/Cartaz')
def cartaz():
    config = getConfig()
    return render_template('cartaz.html', title = "Criação de cartazes", config = config)
@app.route('/getListaDeTemas', methods=['GET', 'POST'])
def getListaDeTemas():
    temas = getThemes()
    return jsonify(temas)
@app.route('/atualizarTema/<tema>', methods=['GET'])
def atualizar_tema(tema):
    updateConfig("Tema_Escolhido", tema)
    return redirect(url_for('cartaz'))
# @app.route('/Cartaz2')
# def cartaz2():
#     return gerar_Exemplar_Vertical()

# =================== Tela de promocoes ===================
@app.route('/Promocao')
def promocao():
    itens = getPromo()
    return render_template('promocao.html', title = "Lista de Itens", itens = itens)
@app.route('/adicionarPromocaoSimples', methods=['GET', 'POST'])
def adicionarPromocaoSimples():
    if request.method == 'POST':
        data = request.json
        nome = data.get('nome')
        valor = data.get('valor')
        addItem(nome, valor)
    return ""
@app.route('/adicionarListaDePromocao', methods=['GET', 'POST'])
def adicionarListaDePromocao():
    if request.method == 'POST':
        data = request.json
        promocoes = data.get('dados')
        for item in promocoes:
            addItem(item[0], item[1])
    return ""
@app.route('/editarListaDePromocao', methods=['GET', 'POST'])
def editarListaDePromocao():
    if request.method == 'POST':
        data = request.json
        promocoes = data.get('dados')
        updateLista(promocoes)
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8221, debug=True)
    
criar_Modelo()