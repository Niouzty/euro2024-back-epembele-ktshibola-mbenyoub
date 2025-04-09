from typing import List

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
            connection.close()
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
    def get_all_entraineurs() -> list[Entraineur]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM entraineur"
            cursor.execute(sql)
            result = cursor.fetchall()
            return [Entraineur(**row) for row in result]
