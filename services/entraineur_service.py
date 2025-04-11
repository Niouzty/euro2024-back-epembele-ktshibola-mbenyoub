from typing import List, Tuple
from models.entraineur_model import Entraineur
from shared.db_connection import get_db_connection

class EntraineurService:

    @staticmethod
    def add_entraineur(nom: str, prenom: str, id_nationalite: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "INSERT INTO entraineur (nom, prenom, id_nationalite) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nom, prenom, id_nationalite))
            connection.commit()
            return True

    @staticmethod
    def delete_entraineur(id_entraineur: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "DELETE FROM entraineur WHERE id_entraineur = %s"
            cursor.execute(sql, (id_entraineur,))
            connection.commit()
            return cursor.rowcount > 0

    @staticmethod
    def get_entraineur(id_entraineur: int) -> Entraineur:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM entraineur WHERE id_entraineur = %s"
            cursor.execute(sql, (id_entraineur,))
            result = cursor.fetchone()
            return Entraineur(**result) if result else None

    @staticmethod
    def get_all_entraineurs(page: int = 1, per_page: int = 10) -> list[Entraineur]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            # Calculer l'offset
            offset = (page - 1) * per_page

            # Récupérer les entraîneurs avec pagination
            sql = "SELECT * FROM entraineur ORDER BY id_entraineur LIMIT %s OFFSET %s"
            cursor.execute(sql, (per_page, offset))
            result = cursor.fetchall()
            entraineurs = [Entraineur(**row) for row in result]

            return entraineurs

    @staticmethod
    def get_number_row() -> int:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Échec de la connexion à la base de données.")
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(*) FROM entraineur"
            cursor.execute(sql)
            row = cursor.fetchone()
            return row['COUNT(*)'] if row else 0