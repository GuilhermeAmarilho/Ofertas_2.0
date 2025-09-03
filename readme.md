# 🛒 Ofertas Amarilho

## Sistema de Gerador de Cartazes

Projeto pessoal desenvolvido para automatizar o processo de busca, organização e exibição de imagens de produtos, com integração para geração de cartazes promocionais para o **Mercado Amarilho**.

---

## 📂 Estrutura do Projeto

- [📁 Estrutura do Projeto](Documentacao/estrutura.md)

---

## ⚙️ Funcionalidades

- 🔍 **Três modos de busca de imagem por item:**
  1. **Busca local** no banco de dados interno, com correspondência de nomes baseada em similaridade, utilizando a biblioteca `fuzzywuzzy`.
  2. **Busca online via API do Google Custom Search**, realizando uma pesquisa programática com base no nome do item, com opção de filtros como tipo, tamanho e cor da imagem.
  3. **Busca via scraping com Selenium**, simulando um navegador real para acessar o Google Imagens, extrair miniaturas e apresentar opções visuais.

- 🧠 O sistema realiza a **busca em etapas**, priorizando a fonte mais eficiente:
  - Primeiro tenta encontrar a imagem **localmente**;
  - Se não encontrar, parte para a **API do Google**;
  - E como último recurso, utiliza o **scraping com Selenium**.

- 🖼️ **Exibição automática das imagens** usando a biblioteca `Pillow`, com opção de visualizar, selecionar ou salvar a imagem desejada.

- 🧪 **Ambiente virtual isolado (`virtualenv`)**, garantindo portabilidade e fácil replicação do projeto. As dependências estão organizadas no arquivo `requirements.txt`.

- 📂 **Organização modular por pastas**, com separação clara entre funcionalidades: `Cartaz`, `Encarte`, `Image_Location`, `Scraping`, `Storage`, `Web`, entre outras.

---

## 📦 Requisitos

- Python 3.10+
- [virtualenv](https://virtualenv.pypa.io/)
- Navegador Google Chrome (para scraping com Selenium)
- WebDriver compatível com sua versão do Chrome

---

## 🔧 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/GuilhermeAmarilho/Ofertas_2.0
cd Ofertas_2.0
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. 🔐 Variáveis de ambiente

- É necessário criar o arquivo .env manualmente na raiz do projeto com as seguintes chaves:

```env
GOOGLE_SEARCH_API_KEY=<sua_api_key>
GOOGLE_SEARCH_API_ENGINE=<seu_engine_id>
```

- 🔔 Observação: Essas chaves são usadas para realizar buscas automáticas de imagens via Google Programmable Search Engine (JSON API).

### 5. ▶️ Como rodar

```bash
python main.py
```

---

## 🛠️ Tarefas em andamento

### 