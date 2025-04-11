from typing import List

from models.joueur_model import Joueur
from shared.db_connection import get_db_connection

class JoueurService:

    @staticmethod
    def add_joueur(nom: str, prenom: str, date_naissance: str, id_nationalite: int, id_poste: int, num_maillot: int, id_equipe: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO joueur (nom, prenom, date_naissance, id_nationalite, id_poste, num_maillot, id_equipe)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (nom, prenom, date_naissance, id_nationalite, id_poste, num_maillot, id_equipe))
            connection.commit()
            return True

    @staticmethod
    def delete_joueur(id_joueur: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "DELETE FROM joueur WHERE id_joueur = %s"
            cursor.execute(sql, (id_joueur,))
            connection.commit()
            return cursor.rowcount > 0

    @staticmethod
    def get_joueur(id_joueur: int) -> Joueur:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM joueur WHERE id_joueur = %s"
            cursor.execute(sql, (id_joueur,))
            result = cursor.fetchone()
            return Joueur(**result) if result else None

    @staticmethod
    def get_joueurs(offset: int, limit: int) -> list[Joueur]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Échec de la connexion à la base de données.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM joueur LIMIT %s OFFSET %s"
            cursor.execute(sql, (limit, offset))
            rows = cursor.fetchall()
            return [Joueur(**row) for row in rows]

    @staticmethod
    def get_number_row() -> int:
        conn = get_db_connection()
        if not conn:
            raise ConnectionError("Connexion à la base de données échouée.")

        with conn.cursor() as cursor:
            query = "SELECT COUNT(*) FROM joueur"
            cursor.execute(query)
            result = cursor.fetchone()
            return result['COUNT(*)'] if result else 0