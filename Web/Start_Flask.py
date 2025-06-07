from flask import Flask
from .Routes.Home import home_bp
from .Routes.Cartaz import cartaz_bp
# from rotas.promocao import promocao_bp

app = Flask(__name__)

# Registrar todos os blueprints
app.register_blueprint(home_bp)
app.register_blueprint(cartaz_bp)
# app.register_blueprint(promocao_bp)