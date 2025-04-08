from utils.db_connection import get_db_connection

class PosteService:

    @staticmethod
    def add_poste(nom_poste: str) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "INSERT INTO poste (nom_poste) VALUES (%s)"
            cursor.execute(sql, (nom_poste,))
            connection.commit()
            return True

    @staticmethod
    def delete_poste(id_poste: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "DELETE FROM poste WHERE id_poste = %s"
            cursor.execute(sql, (id_poste,))
            connection.commit()
            return cursor.rowcount > 0

    @staticmethod
    def get_poste(id_poste: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM poste WHERE id_poste = %s"
            cursor.execute(sql, (id_poste,))
            return cursor.fetchone()

    @staticmethod
    def get_all_postes() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM poste"
            cursor.execute(sql)
            return cursor.fetchall()
