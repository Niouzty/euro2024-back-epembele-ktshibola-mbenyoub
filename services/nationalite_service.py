
from models.nationalite_model import Nationalite
from shared.db_connection import get_db_connection


class NationaliteService:

    @staticmethod
    def add_nationalite(nom: str) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "INSERT INTO nationalite (nom) VALUES (%s)"
            cursor.execute(sql, (nom,))
            connection.commit()
            return True

    @staticmethod
    def delete_nationalite(id_nationalite: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "DELETE FROM nationalite WHERE id_nationalite = %s"
            cursor.execute(sql, (id_nationalite,))
            connection.commit()
            return cursor.rowcount > 0

    @staticmethod
    def get_nationalite(id_nationalite: int) -> Nationalite | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM nationalite WHERE id_nationalite = %s"
            cursor.execute(sql, (id_nationalite,))
            result = cursor.fetchone()
            return Nationalite(**result) if result else None

    @staticmethod
    def get_nationalites(offset: int, limit: int) -> list[Nationalite]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Échec de la connexion à la base de données.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM nationalite LIMIT %s OFFSET %s"
            cursor.execute(sql, (limit, offset))
            rows = cursor.fetchall()
            return [Nationalite(**row) for row in rows]

    @staticmethod
    def get_number_row() -> int:
        conn = get_db_connection()
        if not conn:
            raise ConnectionError("Connexion à la base de données échouée.")

        with conn.cursor() as cursor:
            query = "SELECT COUNT(*) FROM nationalite"
            cursor.execute(query)
            result = cursor.fetchone()
            return result['COUNT(*)'] if result else 0