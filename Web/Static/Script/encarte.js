document.addEventListener("DOMContentLoaded", () => {
    const itens = document.querySelectorAll(".Item_Content");
    itens.forEach(item => {
        item.addEventListener("click", () => {

            const id = item.getAttribute("id");
            const nome = item.querySelector(".Item_Name")?.textContent;
            if (nome != undefined){
                document.querySelector('div.Img h1').innerHTML = nome
                console.log("Item clicado:", { id, nome })
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
    .then(
        response => response.json()
            .then(
                data => {
                    console.log("Resposta:", data);
                }
            )
        )
    .catch(
        err => console.error(
            "Erro:",
            err
        )
    );
}