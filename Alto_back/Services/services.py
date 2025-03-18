from Modeles.modele import *
from flask_jwt_extended import create_access_token
from peewee import *
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
def verif_nom_utilisateur(nom):
    try:
        utilisateur.get(utilisateur.nom_utilisateur==nom)
        return True
    except DoesNotExist:
        return False
    
def verif_mdp_utilisateur(nom, mdp):
        uti = utilisateur.get(utilisateur.nom_utilisateur==nom,)
        return bcrypt.check_password_hash(uti.mdp_utilisateur, mdp)
       
    
def creation_jeton(nom):
    info=utilisateur.get(utilisateur.nom_utilisateur==nom)
    donnees = {
        'id_utilisateur':info.id_utilisateur,
        'id_role':info.id_role
    }
    jeton = create_access_token(identity=info.nom_utilisateur,additional_claims=donnees)
    return jeton

def creation_utilisateur(nom, mdp, role):
    mdp_hash = bcrypt.generate_password_hash(mdp).decode('utf-8')  # Hachage et conversion en chaîne de caractères
    utilisateur.create(nom_utilisateur=nom, mdp_utilisateur=mdp_hash, id_role=role)
