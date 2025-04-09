from typing import List

from models.groupe_model import Groupe
from shared.db_connection import get_db_connection

class GroupeService:

    @staticmethod
    def add_groupe(nom: str) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "INSERT INTO groupe (nom) VALUES (%s)"
            cursor.execute(sql, (nom,))
            connection.commit()
            return True

    @staticmethod
    def delete_groupe(id_groupe: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "DELETE FROM groupe WHERE id_groupe = %s"
            cursor.execute(sql, (id_groupe,))
            connection.commit()
            return cursor.rowcount > 0

    @staticmethod
    def get_groupe(id_groupe: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM groupe WHERE id_groupe = %s"
            cursor.execute(sql, (id_groupe,))
            result = cursor.fetchone()
            return Groupe(**result) if result else None

    @staticmethod
    def get_all_groupes() -> list[Groupe]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM groupe"
            cursor.execute(sql)
            result = cursor.fetchall()
            return [Groupe(**row) for row in result]