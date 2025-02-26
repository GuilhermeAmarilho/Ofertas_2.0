// Adicionar itens
const div_Adicionar_Promocao = document.querySelector('div#adicionar_Promocao');
const background_Adicionar_Promocao = document.querySelector('div#background_Adicionar_Promocao');
background_Adicionar_Promocao.addEventListener(
    "click", function (e) {
        div_Adicionar_Promocao.classList.toggle('adicionar_Promocao');
        div_Adicionar_Promocao.classList.toggle('adicionar_Promocao_Fechado');
        background_Adicionar_Promocao.classList.toggle('background_Adicionar_Promocao');
        background_Adicionar_Promocao.classList.toggle('background_Adicionar_Promocao_Fechado');
    }
);
function tela_Adicionar_Promocao(){
    div_Adicionar_Promocao.classList.toggle('adicionar_Promocao');
    div_Adicionar_Promocao.classList.toggle('adicionar_Promocao_Fechado');
    background_Adicionar_Promocao.classList.toggle('background_Adicionar_Promocao');
    background_Adicionar_Promocao.classList.toggle('background_Adicionar_Promocao_Fechado');
}
function adicionar_Promocao_Enviar(){
    nome = document.querySelector('input[name=Nome]');
    valor = document.querySelector('input[name=Valor]');
    if (!isNaN(parseFloat(valor.value)) && nome.value != ''){
        fetch('/adicionarPromocaoSimples', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ nome: nome.value, valor: valor.value }),
        })
        .then(() => window.location.href = '/Promocoes');         
    }else{
        if(isNaN(parseFloat(valor.value))){
            valor.setCustomValidity('Por favor, insira um valor válido.');
        }else{
            valor.setCustomValidity('');
        }
        if(nome.value == ''){
            nome.setCustomValidity('Campo nome não pode ser vazio.');
        }
        else{
            nome.setCustomValidity('');
        }
    }
}
tela_Adicionar_Promocao(); // Fechar a tela via js
// Adicionar lista de itens
const div_Adicionar_Lista = document.querySelector('div#adicionar_Lista');
const background_Adicionar_Lista = document.querySelector('div#background_Adicionar_Lista');
const textarea_Adicionar_Lista = document.querySelector('#Inserir_Lista');
background_Adicionar_Lista.addEventListener(
    "click", function (e) {
        div_Adicionar_Lista.classList.toggle('adicionar_Lista');
        div_Adicionar_Lista.classList.toggle('adicionar_Lista_Fechado');
        background_Adicionar_Lista.classList.toggle('background_Adicionar_Lista');
        background_Adicionar_Lista.classList.toggle('background_Adicionar_Lista_Fechado');
    }
);
const tamanho_Base_Textarea_Adicionar_Lista = parseFloat(window.getComputedStyle(textarea_Adicionar_Lista).height);
textarea_Adicionar_Lista.addEventListener(
    'keydown', function (e) {
        font_Size_Tela_Lista_De_Promocao = parseFloat(window.getComputedStyle(textarea_Adicionar_Lista).fontSize);
        regex = new RegExp('\n', 'g');
        matches = textarea_Adicionar_Lista.value.match(regex);
        num_Linhas = (matches ? matches.length : 0);
        textarea_Adicionar_Lista.style.height = (
            tamanho_Base_Textarea_Adicionar_Lista + 
            font_Size_Tela_Lista_De_Promocao * 1.15 * num_Linhas
        ) + 'px';
    }
)
function tela_Lista_De_Promocao(){
    div_Adicionar_Lista.classList.toggle('adicionar_Lista');
    div_Adicionar_Lista.classList.toggle('adicionar_Lista_Fechado');
    background_Adicionar_Lista.classList.toggle('background_Adicionar_Lista');
    background_Adicionar_Lista.classList.toggle('background_Adicionar_Lista_Fechado');
}
function lista_De_Promocao_Limpar(){
    textarea_Adicionar_Lista.value = '';
    textarea_Adicionar_Lista.style.height = (tamanho_Base_Textarea_Adicionar_Lista) + 'px';
}
function lista_De_Promocao_Enviar(){
    dados = textarea_Adicionar_Lista.value.split("\n");
    promocoes = [];
    erro = false;
    for (let i = 0; i < dados.length; i++) {
        let nome = dados[i].split(' ');
        let valor = nome.pop();
        nome = nome.join(' ');
        if(isNaN(parseFloat(valor)) || dados == [''] || nome == ''){
            erro = true;
        }else{
            promocoes.push([nome, valor]);
        }
    }
    if (erro){
        textarea_Adicionar_Lista.setCustomValidity('Por favor, insira um valor válido.');
    }else{
        textarea_Adicionar_Lista.setCustomValidity('');
        fetch('/adicionarListaDePromocao', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ dados: promocoes}),
        })
        .then(() => window.location.href = '/Promocoes');
    }
}
tela_Lista_De_Promocao(); // Fechar a tela via js
// Editar lista de itens
if (document.querySelector('div#editar_Lista') != null){
    const div_Editar_Lista = document.querySelector('div#editar_Lista');
    const background_Editar_Lista = document.querySelector('div#background_Editar_Lista');
    const textarea_Editar_Lista = document.querySelector('#Editar_Lista');
    background_Editar_Lista.addEventListener(
        "click", function (e) {
            div_Editar_Lista.classList.toggle('editar_Lista');
            div_Editar_Lista.classList.toggle('editar_Lista_Fechado');
            background_Editar_Lista.classList.toggle('background_Editar_Lista');
            background_Editar_Lista.classList.toggle('background_Editar_Lista_Fechado');
        }
    );
    let Tamanho_Base_Textarea_Editar_Lista = parseFloat(window.getComputedStyle(textarea_Editar_Lista).height);
    textarea_Editar_Lista.addEventListener(
        'keydown', function (e) {
            font_Size_Tela_Editar_Lista_De_Promocao= parseFloat(window.getComputedStyle(textarea_Editar_Lista).fontSize);
            regex = new RegExp('\n', 'g');
            matches = textarea_Editar_Lista.value.match(regex);
            num_Linhas = (matches ? matches.length : 0);
            textarea_Editar_Lista.style.height = (
                Tamanho_Base_Textarea_Editar_Lista + 
                font_Size_Tela_Editar_Lista_De_Promocao * 1.15 * num_Linhas
            ) + 'px';
        }
    )
    function tela_Editar_Lista_Promocoes(){
        div_Editar_Lista.classList.toggle('editar_Lista');
        div_Editar_Lista.classList.toggle('editar_Lista_Fechado');
        background_Editar_Lista.classList.toggle('background_Editar_Lista');
        background_Editar_Lista.classList.toggle('background_Editar_Lista_Fechado');
        regex = new RegExp('\n', 'g');
        matches = textarea_Editar_Lista.value.match(regex);
        num_Linhas = (matches ? matches.length : 0);
        console.log(num_Linhas);
        textarea_Editar_Lista.style.height = (
            parseFloat(window.getComputedStyle(textarea_Editar_Lista).height) + 
            parseFloat(window.getComputedStyle(textarea_Editar_Lista).fontSize) * 1.15 * num_Linhas
        ) + 'px';
    }
    function editar_Lista_Promocoes_Limpar(){
        textarea_Editar_Lista.value = "";
        textarea_Editar_Lista.style.height = (tamanho_Base_Textarea_Adicionar_Lista) + 'px';
    }
    function editar_Lista_Promocoes_Enviar(){
        dados = textarea_Editar_Lista.value;
        fetch('/editarListaDePromocao', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ dados: dados}),
        })
        .then(() => window.location.href = '/Promocoes');
    }
    tela_Editar_Lista_Promocoes(); // Fechar a tela via js
}