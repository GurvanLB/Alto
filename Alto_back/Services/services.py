from Modeles.modele import *
from peewee import *

def select_role():
    # Chercher l'utilisateur avec le nom "gurvan" et récupérer son rôle
    resultat = utilisateur.get(utilisateur.nom_utilisateur=="Gurvan")
    role= resultat.id_roles.nom_role 

    # Afficher le nom de l'utilisateur et son rôle
    print(f"Rôle: {role}")
    return role