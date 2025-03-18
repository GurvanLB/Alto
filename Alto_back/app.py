# app.py
import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from configuration import *
from peewee import MySQLDatabase
from flask_cors import CORS

# Créer l'application Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "ma clée secrete bisous"
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
#Initialisation des communications entre les différents port frontend/backend
CORS(app)
# Initialiser DB
db = MySQLDatabase(Param.DB_NAME, user = Param.DB_USER, password = Param.DB_PASSWORD, host = Param.DB_HOST, port = Param.DB_PORT)
db.connect()

#Import des routes
from Controleur.routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000,debug=True)
