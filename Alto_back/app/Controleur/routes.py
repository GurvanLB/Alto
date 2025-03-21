from flask import request, jsonify
from app.Services.SecuriteService import securite  
from app.Services.UtilisateurService import compte
from app import app

@app.route('/', methods=['GET'])
def home():
     return jsonify({'message': 'Accueil de l\'application'})

@app.route('/about', methods=['POST'])
def about():
     compte.verifier_acces_utilisateur()  # Protège cette route avec la vérification du jeton
     return "Page about"

@app.route('/connecter', methods=["POST"])
def connecter():
     donnees = request.get_json()
     # Assure-toi que 'compte' est défini correctement dans le bon fichier de service
     util = compte(donnees["nom"])  # Tu dois avoir une classe 'compte' dans un service approprié
     return util.connexion(donnees["mdp"])

@app.route('/deconnecter', methods=["POST"])
def deconnecter():
     cookie = securite.retirer_jeton()  # Déconnecter l'utilisateur et retirer le jeton
     return cookie

@app.route('/ajout_utilisateur', methods=["POST"])
def ajout_utilisateur():
     donnees = request.get_json()
     # Assure-toi que tu as la fonction 'creer_utilisateur' définie correctement
     return compte.creer_utilisateur(donnees["nom"], donnees["mdp"], donnees["role"])

@app.route('/supprimer_utilisateur', methods=["POST"])
def supprimer_utilisateur():
     donnees = request.get_json()
     # Assure-toi que tu as la fonction 'supprimer_utilisateur' définie correctement
     return compte.supprimer_utilisateur(donnees["nom"])

@app.route('/info_utilisateur', methods=["GET"])
def verification_():
     return compte.requete_info_utilisateur()

@app.route('/verifier_acces', methods=["POST"])
def verification_acces_utilisateur():
     return compte.requete_verifier_acces(1)

@app.route('/ping', methods=["GET"])
def ping():
     return jsonify({"message":"Serveur ok"}),200