from typing import List
from shared.db_connection import get_db_connection
from models.drapeau_model import Drapeau

class DrapeauService:

    @staticmethod
    def add_drapeau(id_equipe: int, chemin_image: str) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")

        with connection.cursor() as cursor:
            sql = "INSERT INTO drapeau (id_equipe, chemin_image) VALUES (%s, %s) RETURNING id_drapeau"
            cursor.execute(sql, (id_equipe, chemin_image))
            connection.commit()
            return True

    @staticmethod
    def delete_drapeau(id_drapeau: int) -> int:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")

        with connection.cursor() as cursor:
            sql = "DELETE FROM drapeau WHERE id_drapeau = %s"
            cursor.execute(sql, (id_drapeau,))
            connection.commit()
            return cursor.rowcount

    @staticmethod
    def get_drapeau(id_drapeau: int) -> Drapeau | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")

        with connection.cursor() as cursor:
            sql = "SELECT id_drapeau, id_equipe, chemin_image FROM drapeau WHERE id_drapeau = %s"
            cursor.execute(sql, (id_drapeau,))
            row = cursor.fetchone()
            if row:
                return Drapeau(**row)
            return None

    @staticmethod
    def get_all_drapeaux(offset: int = 0, limit: int = 10) -> list[Drapeau]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")

        with connection.cursor() as cursor:
            sql = "SELECT * FROM drapeau LIMIT %s OFFSET %s"
            cursor.execute(sql, (limit, offset))
            rows = cursor.fetchall()
            return [Drapeau(**row) for row in rows]

    @staticmethod
    def get_number_row() -> int:
        conn = get_db_connection()
        if not conn:
            raise ConnectionError("Connexion à la base de données échouée.")

        with conn.cursor() as cursor:
            query = "SELECT COUNT(*) FROM drapeau"
            cursor.execute(query)
            result = cursor.fetchone()
            return result['COUNT(*)'] if result else 0