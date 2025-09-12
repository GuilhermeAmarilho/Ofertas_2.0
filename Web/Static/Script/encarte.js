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
    .then(response => response.json())
    .then(data => {
        if (data.length > 0){
            div_Img = document.querySelector('div.Img_Query');
            
            var div_Local_Img_Query = document.createElement('div');
            div_Local_Img_Query.className = "Local_Img_Query";
            
            var p = document.createElement('p');
            p.textContent = "Imagens salvas no banco de dados";
            div_Local_Img_Query.appendChild(p);
            
            var Img_extern_content = document.createElement("div");
            Img_extern_content.className = "Img_extern_content";
            for (let i = 0; i < data.length; i++) {
                url = data[i].split('\\')
                size = url.length;
                url = "\\" + url[size-2] + '\\' + url[size-1]

                var div_Img_Content = document.createElement("div");
                div_Img_Content.className = "Img_Content";

                var a = document.createElement('a');
                var img = document.createElement('img');
                img.src = url;
                
                a.appendChild(img);
                div_Img_Content.appendChild(a);
                Img_extern_content.appendChild(div_Img_Content);
            }
            div_Local_Img_Query.appendChild(Img_extern_content);
            div_Img.appendChild(div_Local_Img_Query);
        }

        
        // document.querySelector("#img").src = url;
        // document.querySelector("#score").textContent = `${score}%`;
    })       
    .catch(
        err => console.error(
            "Erro:",
            err
        )
    );
}

// function create_Img_Section(titulo, class, img)