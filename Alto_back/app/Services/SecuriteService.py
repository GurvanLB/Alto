from flask_jwt_extended import create_access_token, get_jwt_identity, verify_jwt_in_request, JWTManager, get_jwt
from flask import jsonify, make_response
from datetime import timedelta
from app.configuration import Param
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()

class securite:
    def __init__(self, app):
        """Classe pour gérer la sécurité de l'application (JWT, authentification)."""
        
        jwt = JWTManager()
        app.config["JWT_SECRET_KEY"] = "ta_cle_secrete"  # Remplace par une clé sécurisée
        jwt.init_app(app)
    

    @staticmethod
    def creer_jeton(utilisateur):
        """
        Crée un token JWT pour un utilisateur donné.
        :param utilisateur: Objet utilisateur contenant les infos
        :return: Token JWT sous forme de chaîne de caractères
        """
        donnees = {
            'id_utilisateur': utilisateur.id,
            'id_role': utilisateur.id_role
        }
        return create_access_token(
            identity=utilisateur.nom,
            additional_claims=donnees,
            expires_delta=timedelta(hours=2)
        )
    

    @staticmethod
    def retirer_jeton():
        """
        Déconnecte l'utilisateur en supprimant le cookie.
        :return: Réponse HTTP avec message de déconnexion
        """
        response = make_response(jsonify({"message": "Déconnexion réussie"}), 200)
        response.delete_cookie('token')
        return response

    @staticmethod
    def requete_jeton(utilisateur):
        """
        Génère la réponse HTTP après une connexion réussie avec le jeton inclus.
        :param utilisateur: Objet utilisateur
        :return: Réponse Flask avec cookie sécurisé
        """
        jeton = securite.creer_jeton(utilisateur)
        response = make_response(jsonify({"message": "Connexion réussie", "nom": utilisateur.nom,"error":False}), 200)
        response.set_cookie('token', jeton, httponly=True, secure=False, samesite='Lax', path='/')
        return response

    @staticmethod
    def recuperation_info_jeton():
        """
        Middleware pour protéger les routes.
        Si le jeton est invalide, renvoie une erreur.
        """
        try:
            securite.verifier_acces()
            nom_utilisateur = get_jwt_identity()
            info = get_jwt()
            id_utilisateur = info.get('id_utilisateur') 
            id_role_utilisateur = info.get('id_role') 
            return id_utilisateur, id_role_utilisateur, nom_utilisateur
        except Exception as e:
            id_utilisateur=""
            id_role_utilisateur="" 
            nom_utilisateur=""
            return id_utilisateur, id_role_utilisateur, nom_utilisateur
    @staticmethod
    def verifier_acces():
        """
        Middleware pour protéger les routes.
        Si le jeton est invalide, renvoie une erreur.
        """
        try:
            verify_jwt_in_request()
            return jsonify({"message": "Accès autorisé", "error":False}), 200
        except  Exception as e:
            return jsonify({"message": "Accès non autorisé", "error":True}), 401
        
    
    @staticmethod
    def verifier_mdp_utihacher(mdp, mdp_hacher):
        """
        Vérifie le mot de passe d'un utilisateur donné.
        :param nom: Nom de l'utilisateur
        :param mdp: Mot de passe à vérifier
        :return: True si le mot de passe est correct, False sinon
        """
        
        return bcrypt.check_password_hash(mdp_hacher, mdp)
    
    @staticmethod
    def hachage_mdp(mdp):
        """
        Hache un mot de passe en utilisant bcrypt.
        :param mdp: Mot de passe à hacher
        :return: Chaîne de caractères hachée
        """
        return bcrypt.generate_password_hash(mdp).decode('utf-8')