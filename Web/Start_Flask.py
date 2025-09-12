from flask import Flask, abort, send_from_directory
from .Routes.Home import home_bp
from .Routes.Cartaz import cartaz_bp
from .Routes.Encarte import encarte_bp
from .Routes.Promocao import promocao_bp

app = Flask(__name__)

# caminho absoluto da sua pasta
ITEMS_IMAGE_DIR = r"C:\Users\gui\Documents\Codigos\Crie_Ofertas\Items_Image"

@app.route("/Items_Image/<path:filename>")
def items_image(filename):
    try:
        return send_from_directory(ITEMS_IMAGE_DIR, filename)
    except FileNotFoundError:
        abort(404)
        
# Registrar todos os blueprints
app.register_blueprint(home_bp)
app.register_blueprint(cartaz_bp)
app.register_blueprint(encarte_bp)
app.register_blueprint(promocao_bp)