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
        fetch('/Promocao/AdicionarPromocaoSimples', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ nome: nome.value, valor: valor.value }),
        })
        .then(() => window.location.href = '/Promocao');         
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
        if(!(isNaN(parseFloat(valor)) || dados == [''] || nome == '')){
            promocoes.push([nome, valor]);
        }
    }
    if (promocoes.length>0){
        textarea_Adicionar_Lista.setCustomValidity('');
        fetch('/Promocao/AdicionarListaDePromocao', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ dados: promocoes}),
        })
        .then(() => window.location.href = '/Promocao');
    }
}

// Fechar a tela via js
tela_Lista_De_Promocao(); 

// Botões alterar e remover itens 
function remover_Item(item){
    fetch('/Promocao/RemoverItemPromocao', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id: item}),
        })
        .then(() => window.location.href = '/Promocao');
}
const div_Alterar_Promocao = document.querySelector('div#alterar_Promocao');
const background_Alterar_Promocao = document.querySelector('div#background_Alterar_Promocao');
background_Alterar_Promocao.addEventListener(
    "click", function (e) {
        div_Alterar_Promocao.classList.toggle('alterar_Promocao');
        div_Alterar_Promocao.classList.toggle('alterar_Promocao_Fechado');
        background_Alterar_Promocao.classList.toggle('background_Alterar_Promocao');
        background_Alterar_Promocao.classList.toggle('background_Alterar_Promocao_Fechado');
    }
);
function tela_Alterar_Promocao(id = null){
    if(id==null){
        div_Alterar_Promocao.classList.toggle('alterar_Promocao');
        div_Alterar_Promocao.classList.toggle('alterar_Promocao_Fechado');
        background_Alterar_Promocao.classList.toggle('background_Alterar_Promocao');
        background_Alterar_Promocao.classList.toggle('background_Alterar_Promocao_Fechado');
    }else{
        nome = document.getElementById("item_Promocao_"+id).children[1].innerHTML;
        valor = document.getElementById("item_Promocao_"+id).children[2].innerHTML;
        document.getElementById('Tela_Alterar_Nome').value = nome;
        valor = valor.replace(",",".");
        document.getElementById('Tela_Alterar_Valor').value = parseFloat(valor);
        tela_Alterar_Promocao();
    }
}
function alterar_Promocao_Enviar(){
    nome = document.querySelector('input[name=Tela_Alterar_Nome]').value;
    valor = document.querySelector('input[name=Tela_Alterar_Valor]').value;
    console.log(nome, valor);
    
    // if (!isNaN(parseFloat(valor.value)) && nome.value != ''){
    //     fetch('/Promocao/AlterarPromocaoSimples', {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/json',
    //         },
    //         body: JSON.stringify({ nome: nome.value, valor: valor.value }),
    //     })
    //     .then(() => window.location.href = '/Promocao');         
    // }else{
    //     if(isNaN(parseFloat(valor.value))){
    //         valor.setCustomValidity('Por favor, insira um valor válido.');
    //     }else{
    //         valor.setCustomValidity('');
    //     }
    //     if(nome.value == ''){
    //         nome.setCustomValidity('Campo nome não pode ser vazio.');
    //     }
    //     else{
    //         nome.setCustomValidity('');
    //     }
    // }
}
tela_Alterar_Promocao()