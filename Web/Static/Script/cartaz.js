
const div_Alterar_Tema = document.querySelector('div#alterar_Tema');
const background_Alterar_Tema = document.querySelector('div#Alterar_Tema_Background');
background_Alterar_Tema.addEventListener(
    "click", function (e) {
        tela_Lista_De_Promocao()
    }
);
function limpar_Lista_De_Temas(){
    while (div_Lista_De_Temas.childElementCount > 0) {
        div_Lista_De_Temas.removeChild(div_Lista_De_Temas.firstChild);
    }
}
function tela_Lista_De_Promocao(){
    limpar_Lista_De_Temas();
    pegar_Temas('');
    document.body.classList.toggle('cartaz_Blocked');
    div_Alterar_Tema.classList.toggle('alterar_Tema');
    div_Alterar_Tema.classList.toggle('alterar_Tema_Fechado');
    background_Alterar_Tema.classList.toggle('Alterar_Tema_Background');
    background_Alterar_Tema.classList.toggle('Alterar_Tema_Background_Fechado');
}
function pegar_Temas(query){
    fetch('/Cartaz/getListaDeTemas')
    .then(response => {return response.json();})
    .then(
        data => {
            for (let index = 0; index < data.length; index++) {
                const tema = data[index];
                if (query == ''){
                    desenhar_Temas(tema);
                }else{
                    query = query.replace(' ', '_').toLowerCase();
                    if (tema.toLowerCase().split(query).length > 1){
                        desenhar_Temas(tema);
                    }
                }
            }                
        }
    )
}
const div_Lista_De_Temas = document.querySelector('div.alterar_Tema_Results');
function desenhar_Temas(tema){
    let tema_Unitario = document.createElement('a');
    tema_Unitario.href = '/Cartaz/atualizarTema/'+tema;
    tema_Unitario.classList = 'alterar_Tema_Unitario';
    let content = document.createElement('p');
    content.textContent = tema.replace(/_/g, " ");
    tema_Unitario.appendChild(content);
    let img = document.createElement('img')
    img.src = "/static/Assets/Themes/" + tema + "/Paisagem.png";
    tema_Unitario.appendChild(img)
    div_Lista_De_Temas.appendChild(tema_Unitario)
}
const query_Input = document.querySelector('input.alterar_Tema_Query');
query_Input.addEventListener(
    'keyup', function (e) {
        limpar_Lista_De_Temas();
        pegar_Temas(query_Input.value)
    }
)

// ###################### ALTERAR LOGO ######################

const div_Alterar_Logo = document.querySelector('div#Alterar_Logo');
const background_Alterar_Logo = document.querySelector('div#Alterar_Logo_Background');
background_Alterar_Logo.addEventListener(
    "click", function (e) {
        tela_Ajuste_Logo()
    }
);
function tela_Ajuste_Logo(){
    document.body.classList.toggle('cartaz_Blocked');
    div_Alterar_Logo.classList.toggle('Alterar_Logo');
    div_Alterar_Logo.classList.toggle('Alterar_Logo_Fechado');
    background_Alterar_Logo.classList.toggle('Alterar_Logo_Background');
    background_Alterar_Logo.classList.toggle('Alterar_Logo_Background_Fechado');
}