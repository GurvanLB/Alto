from flask import Flask
from flask_cors import CORS
from app.Services.SecuriteService import securite

#INITIALISATION DE L'APPLICATION
app = Flask(__name__)
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
#INITIALISATION DE LA SECURITE
securite(app)
#INITIALISATION DES ROUTES
from app.Controleur.routes import *
#INITIALISATION DE CORS
CORS(app, supports_credentials=True, origins="http://localhost:5173")
    
