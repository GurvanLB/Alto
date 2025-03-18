
from app import app
from Services.services import *
from flask import jsonify, request, make_response
from flask_jwt_extended import jwt_required
@app.route('/', methods=['GET'])
def home():
     resultat=select_role()
     return jsonify({'role': resultat})


@app.route('/about', methods=['POST'])
@jwt_required()
def about():
     return "Page about"

@app.route('/connecter', methods=["POST"])
def connecter():
     donnees = request.get_json()
     if verif_nom_utilisateur(donnees["nom"]):
          if verif_mdp_utilisateur(donnees["nom"],donnees["mdp"]):
               jeton = creation_jeton(donnees["nom"])
               cookie = make_response(jsonify({"message":"Connexion réussie","nom":donnees["nom"] }),200)
               cookie.set_cookie('token',jeton, httponly=True,secure=False, samesite='None')
               return cookie
          else:
               return jsonify({"message":"Mot de passe incorrect"}),401
     else:     
          return jsonify({"message":"Utilisateur non trouvé"}),404

@app.route('/deconnecter', methods=["POST"])
def deconnecter():
     cookie = make_response(jsonify({"message":"Déconnexion réussie"}),200)
     cookie.delete_cookie('token')
     return cookie

@app.route('/ajout_utilisateur', methods=["POST"])
def ajout_utilisateur():
     donnees = request.get_json()
     if verif_nom_utilisateur(donnees["nom"]):
          return jsonify("message: Utilisateur déjà existant")
     else:
          creation_utilisateur(donnees["nom"],donnees["mdp"])
          return jsonify("message: Utilisateur ajouté")  
            