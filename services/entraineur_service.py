from utils.db_connection import get_db_connection

class EntraineurService:

    @staticmethod
    def add_entraineur(nom: str, prenom: str, id_nationalite: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO entraineur (nom, prenom, id_nationalite) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nom, prenom, id_nationalite))
                connection.commit()
                return True
        finally:
            connection.close()

    @staticmethod
    def delete_entraineur(id_entraineur: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM entraineur WHERE id_entraineur = %s"
                cursor.execute(sql, (id_entraineur,))
                connection.commit()
                return cursor.rowcount > 0
        finally:
            connection.close()

    @staticmethod
    def get_entraineur(id_entraineur: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM entraineur WHERE id_entraineur = %s"
                cursor.execute(sql, (id_entraineur,))
                return cursor.fetchone()
        finally:
            connection.close()

    @staticmethod
    def get_all_entraineurs() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM entraineur"
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            connection.close()
