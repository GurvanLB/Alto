import os
from dotenv import load_dotenv, find_dotenv

# Charger les variables d'environnement
load_dotenv(find_dotenv())

class Param:
    # Charger les variables d'environnement
    DB_USER = os.getenv("DB_USER", "None")
    DB_HOST = os.getenv("DB_HOST", "None")
    DB_NAME = os.getenv("DB_NAME", "None")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "None")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    SECRET_KEY = os.getenv("SECRET_KEY", "None")               
