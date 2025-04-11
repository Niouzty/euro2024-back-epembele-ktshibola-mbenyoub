from typing import List

from models.ville_model import Ville
from shared.db_connection import get_db_connection

class VilleService:

    @staticmethod
    def add_ville(nom: str) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "INSERT INTO ville (nom) VALUES (%s)"
            cursor.execute(sql, (nom,))
            connection.commit()
            return True

    @staticmethod
    def delete_ville(id_ville: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "DELETE FROM ville WHERE id_ville = %s"
            cursor.execute(sql, (id_ville,))
            connection.commit()
            return cursor.rowcount > 0

    @staticmethod
    def get_ville(id_ville: int) -> Ville | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM ville WHERE id_ville = %s"
            cursor.execute(sql, (id_ville,))
            result = cursor.fetchone()
            return Ville(**result) if result else None

    @staticmethod
    def get_villes(offset: int, limit: int) -> list[Ville]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Échec de la connexion à la base de données.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM ville LIMIT %s OFFSET %s"
            cursor.execute(sql, (limit, offset))
            rows = cursor.fetchall()
            print(rows)
            return [Ville(**row) for row in rows]

    @staticmethod
    def update_ville(id_ville: int, new_nom: str) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "UPDATE ville SET nom = %s WHERE id_ville = %s"
            cursor.execute(sql, (new_nom, id_ville))
            connection.commit()
            return cursor.rowcount > 0

    @staticmethod
    def get_number_row() -> int:
        conn = get_db_connection()
        if not conn:
            raise ConnectionError("Connexion à la base de données échouée.")

        with conn.cursor() as cursor:
            query = "SELECT COUNT(*) FROM ville"
            cursor.execute(query)
            result = cursor.fetchone()
            return result['COUNT(*)'] if result else 0
