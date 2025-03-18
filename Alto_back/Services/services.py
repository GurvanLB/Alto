from Modeles.modele import *
from flask_jwt_extended import create_access_token
from peewee import *


def verif_nom_utilisateur(nom):
    try:
        utilisateur.get(utilisateur.nom_utilisateur==nom)
        return True
    except DoesNotExist:
        return False
    
def verif_mdp_utilisateur(nom, mdp):
    try:
        utilisateur.get(utilisateur.nom_utilisateur==nom, utilisateur.mdp_utilisateur==mdp)
        return True
    except DoesNotExist:
        return False
    
def creation_jeton(nom):
    info=utilisateur.get(utilisateur.nom_utilisateur==nom)
    donnees = {
        'id_utilisateur':info.id_utilisateur,
        'id_role':info.id_role
    }
    jeton = create_access_token(identity=info.nom_utilisateur,additional_claims=donnees)
    return jeton
