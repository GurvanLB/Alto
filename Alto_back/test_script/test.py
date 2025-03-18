from Modeles.modele import utilisateur, role, db

def main():
    if db.is_closed():
        db.connect()
    
    try:
        # Sélectionner uniquement le nom du rôle de Gurvan sans récupérer tout l'utilisateur
        user = utilisateur.get()
        user_role = user.id_roles.nom_role

        print("Le rôle de Gurvan est :", user_role)
    
    except role.DoesNotExist:
        print("L'utilisateur 'Gurvan' n'a pas été trouvé.")
    
    finally:
        if not db.is_closed():
            db.close()

if __name__ == '__main__':
    main()
