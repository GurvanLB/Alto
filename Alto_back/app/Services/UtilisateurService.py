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
            return jsonify({"message": "Utilisateur non trouvé"}), 404

        if not self.verifier_mot_de_passe(mdp):
            return jsonify({"message": "Mot de passe incorrect"}), 401

        return securite.requete_jeton(self)

    @staticmethod
    def creer_utilisateur(nom, mdp, role):
        """Crée un nouvel utilisateur en BDD"""
        if  not utilisateur.select().where(utilisateur.nom_utilisateur == nom).exists():
            mdp_hash = securite.hachage_mdp(mdp)
            utilisateur.create(nom_utilisateur=nom, mdp_utilisateur=mdp_hash, id_roles=role)
            return jsonify("message: Utilisateur ajouté")
        else:
            return jsonify("message: Utilisateur déjà existant")