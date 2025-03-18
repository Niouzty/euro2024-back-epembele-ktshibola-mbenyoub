import pymysql
import os
import logging
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration des logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Vérification des variables d'environnement
required_env_vars = ["DB_HOST", "DB_PORT", "DB_USER", "DB_PASSWORD", "DB_NAME"]
for var in required_env_vars:
    if not os.getenv(var):
        raise ValueError(f"La variable d'environnement {var} est manquante.")

# Configuration de la base de données
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "db": os.getenv("DB_NAME"),
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
}

def get_db_connection():
    """Établit et retourne une connexion à la base de données."""
    try:
        connection = pymysql.connect(**DB_CONFIG)
        logging.info("Connexion à la base de données réussie.")
        return connection
    except pymysql.MySQLError as e:
        logging.error(f"Erreur lors de la connexion à la base de données : {e}")
        raise  # On lève l'erreur pour ne pas masquer le problème
