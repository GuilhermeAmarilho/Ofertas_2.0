document.addEventListener("DOMContentLoaded", () => {
    const itens = document.querySelectorAll(".Item_Content");
    itens.forEach(item => {
        item.addEventListener("click", () => {
            const id = item.getAttribute("id");
            const nome = item.querySelector(".Item_Name")?.textContent;
            if (nome != undefined){
                document.querySelector('div.Img h1').innerHTML = nome
                document.querySelector('a#google_Query').href = "javascript:requestGoogleImg(\""+nome+"\")"
                document.querySelector('a#web_Query').href = "javascript:requestWebImg(\""+nome+"\")"
                let LocalImg = document.querySelector('div.Img_Query');
                while (LocalImg.childNodes.length > 0) {
                    LocalImg.removeChild(LocalImg.childNodes[0])
                }
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
        const LocalImg = document.querySelector('div.Img_Query');
        if (data.length > 0){
            var div_Local_Img_Query = document.createElement('div');
            div_Local_Img_Query.className = "Local_Img_Query";
            
            var p = document.createElement('p');
            p.textContent = "Imagens do banco de dados";
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
            LocalImg.appendChild(div_Local_Img_Query);
        }else{
            var div_Local_Img_Query = document.createElement('div');
            div_Local_Img_Query.className = "Local_Img_Query";
            
            var p = document.createElement('p');
            p.textContent = "Não foram encontradas imagens refentes a busca!";
            div_Local_Img_Query.appendChild(p);
            LocalImg.appendChild(div_Local_Img_Query);
        }
    })       
    .catch(
        err => console.error(
            "Erro:",
            err
        )
    );
}

function requestGoogleImg(nome){
    fetch("/Encarte/QueryGoogle", {
        method: "POST",
        headers: {
        "Content-Type": "application/json"
        },
        body: JSON.stringify({ nome: nome })
    })
    .then(response => response.json())
    .then(data => {
        const LocalImg = document.querySelector('div.Img_Query');
        console.log(data.length);
        if (document.querySelector('div.Google_Img_Query') != null){

        }else{

            if (data.length > 0){
                var div_Google_Img_Query = document.createElement('div');
                div_Google_Img_Query.className = "Google_Img_Query";
                
                var p = document.createElement('p');
                p.textContent = "Imagens do banco de dados";
                div_Google_Img_Query.appendChild(p);
                
                var Img_extern_content = document.createElement("div");
                Img_extern_content.className = "Img_extern_content";
                for (let i = 0; i < data.length; i++) {
                    var div_Img_Content = document.createElement("div");
                    div_Img_Content.className = "Img_Content";
    
                    var a = document.createElement('a');
                    var img = document.createElement('img');
                    img.src = data[i];
                    
                    a.appendChild(img);
                    div_Img_Content.appendChild(a);
                    Img_extern_content.appendChild(div_Img_Content);
                }
                div_Google_Img_Query.appendChild(Img_extern_content);
                LocalImg.appendChild(div_Google_Img_Query);
            }else{
                var div_Google_Img_Query = document.createElement('div');
                div_Google_Img_Query.className = "Google_Img_Query";
                
                var p = document.createElement('p');
                p.textContent = "Não foram encontradas imagens refentes a busca!";
                div_Google_Img_Query.appendChild(p);
                LocalImg.appendChild(div_Google_Img_Query);
            }
        }
    })       
    .catch(
        err => console.error(
            "Erro:",
            err
        )
    );
}

function requestWebImg(nome){
    console.log(nome);
    
}