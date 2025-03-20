from app.Modeles.modele import utilisateur
from flask import jsonify
from app.Services.SecuriteService import securite


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
    def creer_utilisateur(nom, mdp, role):
        """Crée un nouvel utilisateur en BDD"""
        if  not utilisateur.select().where(utilisateur.nom_utilisateur == nom).exists():
            mdp_hash = securite.hachage_mdp(mdp)
            utilisateur.create(nom_utilisateur=nom, mdp_utilisateur=mdp_hash, id_roles=role)
            return jsonify({"message": "Utilisateur ajouté","error":False}),200
        else:
            return jsonify({"message": "Utilisateur déjà existant","error":True}),400
        
    def recuperer_utilisateur_jeton():
        """Récupère un utilisateur en BDD"""
        id,role,nom=securite.recuperation_info_jeton()
        if (id=="") or (role=="") or (nom==""):
            return jsonify({"message": "Jeton non valide","error":True}),404
        else:
            util= utilisateur.get(utilisateur.nom_utilisateur==nom)
            if util.nom_utilisateur==nom and util.id_utilisateur==id and util.id_role==role:
                #return jsonify({"message:":"je suis ici"})
                return jsonify({"message": "Utilisateur trouvé","error":False,"nom":str(nom),"id":str(id),"role_id":str(role)}),200
            else:
                return jsonify({"message": "Jeton informations non conforme","error":False}),200
    
     