from flask import Flask
from .Routes.Home import home_bp
from .Routes.Cartaz import cartaz_bp
from .Routes.Encarte import encarte_bp
from .Routes.Promocao import promocao_bp

app = Flask(__name__)

# Registrar todos os blueprints
app.register_blueprint(home_bp)
app.register_blueprint(cartaz_bp)
app.register_blueprint(encarte_bp)
app.register_blueprint(promocao_bp)