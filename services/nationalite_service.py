from utils.db_connection import get_db_connection

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
    def get_nationalite(id_nationalite: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM nationalite WHERE id_nationalite = %s"
            cursor.execute(sql, (id_nationalite,))
            return cursor.fetchone()

    @staticmethod
    def get_all_nationalites() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM nationalite"
            cursor.execute(sql)
            return cursor.fetchall()
