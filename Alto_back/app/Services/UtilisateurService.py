from app.Modeles.modele import utilisateur, role
from flask import jsonify , Response
from app.Services.SecuriteService import securite
from app.configuration import Param


class compte:
    def __init__(self, nom):
        """Initialise un utilisateur en cherchant ses infos dans la BDD"""
        try:
            self.compte = utilisateur.get(utilisateur.nom_utilisateur == nom)
            self.id = self.compte.id_utilisateur
            self.nom = self.compte.nom_utilisateur
            self.mdp = self.compte.mdp_utilisateur
            self.id_role = self.compte.id_role
        except utilisateur.DoesNotExist:
            self.compte = None

    def existe(self):
        """Vérifie si l'utilisateur existe"""
        return self.compte is not None

    def verifier_mot_de_passe(self, mdp):
        """Vérifie si le mot de passe correspond"""
        if self.existe():
            return securite.verifier_mdp_utihacher(mdp, self.compte.mdp_utilisateur)
        return False

    def creer_jeton(self):
        """Crée un token JWT pour l'utilisateur"""
        if self.existe():
            donnees = {
                'id_utilisateur': self.id,
                'id_role': self.id_role
            }
            return securite.creer_jeton(self.nom, donnees)
            
        return None

    def connexion(self, mdp):
        """Gère le processus de connexion et renvoie la réponse HTTP avec le jeton"""
        if not self.existe():
            return jsonify({"message": "L'utilisateur n'a pas été trouvé. Veuillez vérifier vos identifiants.","error":True}), 404

        if not self.verifier_mot_de_passe(mdp):
            return jsonify({"message": "Mot de passe incorrect. Veuillez réessayer.","error":True }), 401  # Code HTTP 401 - Unauthorized

        return securite.requete_jeton(self)

    @staticmethod
    def creer_utilisateur(nom, mdp, roled):
        """Crée un nouvel utilisateur en BDD"""
        if  not utilisateur.select().where(utilisateur.nom_utilisateur == nom).exists():
            mdp_hash = securite.hachage_mdp(mdp)

            if not role.select().where(role.id_role == roled).exists():
                return jsonify({"message": "Role non existant","error":True}),400
            utilisateur.create(nom_utilisateur=nom, mdp_utilisateur=mdp_hash, id_roles=roled)
            return jsonify({"message": "Utilisateur ajouté","error":False}),200
        else:
            return jsonify({"message": "Utilisateur déjà existant","error":True}),400
        
    @staticmethod   
    def recuperer_utilisateur_jeton():
        """Récupère un utilisateur en BDD"""
        id, role, nom = securite.recuperation_info_jeton()
        
        # Vérification si les informations du jeton sont valides
        if (id == "") or (role == "") or (nom == ""):
            # Retourner un dictionnaire avec une clé 'error' pour indiquer l'erreur
            return {"message": "Jeton non valide", "error": True}, 401
        else:
            # Recherche de l'utilisateur en BDD
            util = utilisateur.get(utilisateur.nom_utilisateur == nom)
            
            # Vérification des informations utilisateur dans la BDD
            if util.nom_utilisateur == nom and util.id_utilisateur == id and util.id_role == role:
                # Retourner un dictionnaire avec les informations utilisateur
                return {
                    "message": "Utilisateur trouvé",
                    "error": False,
                    "nom": util.nom_utilisateur,
                    "id": util.id_utilisateur,
                    "role_id": util.id_role
                }, 200
            else:
                # Retourner un dictionnaire avec une erreur si les informations sont incorrectes
                return {"message": "Jeton: informations non conformes", "error": True}, 401
            
    @staticmethod  
    def requete_info_utilisateur():
            info,status=compte.recuperer_utilisateur_jeton()
            return jsonify(info),status
    @staticmethod
    def verifier_acces_utilisateur(role_minimum):
        """
        Middleware pour protéger les routes.
        Vérifie si le rôle de l'utilisateur est suffisant, sinon renvoie une erreur.
        """
        information_utilisateur, status_code = compte.recuperer_utilisateur_jeton()
        # Vérifier si l'accès est refusé (si "error" est True)
        if status_code==200:
            if role_minimum==1:
                if securite.verifier_role(information_utilisateur["role_id"], Param.ROLE_ADMIN):
                    return ({"message":"Niveau Autorisé","error":False}), 200
                else:
                    return ({"message":"Niveau d'acces demandé invalide","error":True}), 400
            elif role_minimum==2:
                if securite.verifier_role(information_utilisateur["role_id"], Param.ROLE_ADMIN, Param.ROLE_UTILISATEUR):
                    return ({"message":"Niveau Autorisé","error":False}), 200
                else:
                    return ({"message":"Niveau d'acces invalide", "error":True}), 400
            else:
                return ({"message":"Niveau d'acces saisie erroné","error":True}), 400
        else:
            return (information_utilisateur), 401
        # Vérifier le rôle de l'utilisateur

    @staticmethod  
    def requete_verifier_acces(role_minimum):
        info,status=compte.verifier_acces_utilisateur(role_minimum)
        return jsonify(info),status
