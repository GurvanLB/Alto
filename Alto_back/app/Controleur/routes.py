
from app import app
from app.Services.services import *
from flask import jsonify, request, make_response
from flask_jwt_extended import jwt_required
from app.Modeles.modele import utilisateur
from app.Services.UtilisateurService import utilisateur
from app.Services.SecuriteService import securite
@app.route('/', methods=['GET'])
def home():
     return jsonify({'role'})


@app.route('/about', methods=['POST'])

def about():
     securite.verifier_acces()
     return "Page about"

@app.route('/connecter', methods=["POST"])
def connecter():
     donnees = request.get_json()
     util = utilisateur(donnees["nom"])
     return util.connexion(donnees["mdp"])
     

@app.route('/deconnecter', methods=["POST"])
def deconnecter():
     cookie=securite.retirer_jeton()
     return cookie

@app.route('/ajout_utilisateur', methods=["POST"])
def ajout_utilisateur():
     donnees = request.get_json()
     return utilisateur.creer_utilisateur(donnees["mdp"], donnees["role"])