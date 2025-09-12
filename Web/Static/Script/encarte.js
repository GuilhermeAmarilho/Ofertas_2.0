document.addEventListener("DOMContentLoaded", () => {
    const itens = document.querySelectorAll(".Item_Content");
    itens.forEach(item => {
        item.addEventListener("click", () => {

            const id = item.getAttribute("id");
            const nome = item.querySelector(".Item_Name")?.textContent;
            if (nome != undefined){
                document.querySelector('div.Img h1').innerHTML = nome
                requestQueryImg(nome)
                
            }
        });
    });
});



function requestQueryImg(nome) {
    fetch("/Encarte/QueryImg", {
        method: "POST",
        headers: {
        "Content-Type": "application/json"
        },
        body: JSON.stringify({ nome: nome })
    })
    .then(response => response.json())  // transforma em JSON
    .then(data => {
        // aqui você já tem o data pronto
        console.log("Resposta:", data);

        // exemplo de uso: colocar a imagem no DOM
        const [[url, score]] = data;
        document.querySelector("#img").src = url;
        document.querySelector("#score").textContent = `${score}%`;
    })       
    .catch(
        err => console.error(
            "Erro:",
            err
        )
    );
}