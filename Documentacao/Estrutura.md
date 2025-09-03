# 📁 Estrutura do Projeto
```bash
Ofertas_2.0/
├── Cartaz/
│   └── Cartaz.py
├── Encarte/
│   └── Encarte.py
├── Funcoes_Auxiliares/
│   ├── limpar_pacotes.cmd
│   ├── rename.py
│   └── replace_names.py
├── Image_Location/
│   ├── Find_In_Files.py
│   └── Find_In_Web.py
├── Items_Image/
│   └── ...                # Imagens de produtos
├── Scraping/
│   └── Selenium.py
├── Storage/
│   ├── Config.json
│   ├── Config.py
│   ├── dados_ofertas.txt
│   └── Lista_Promo.py
├── virtual_ofertas/
│   └── ...                # VirtualEnv
├── Web/
│   ├── Routes/
│   │   ├── Cartaz.py
│   │   ├── Encarte.py
│   │   ├── Home.py
│   │   └── Promocao.py
│   ├── Static/
│   │   └── ...            # Arquivos estáticos (CSS, imagens, etc)
│   ├── Templates/
│   │   ├── Generico/      # Templaes reutilizaveis
│   │   ├── cartaz.html
│   │   ├── encarte.html
│   │   ├── index.html
│   │   └── promocao.html
│   └── Start_Flask.py
├── .env                   # Variáveis de ambiente (API Keys)
├── .gitignore             # Git: o que não subir
├── main.py                # Ponto principal de execução
├── readme.md              # Descrição e instruções do projeto
└── requeriments.txt       # Lista de dependências do projeto
```