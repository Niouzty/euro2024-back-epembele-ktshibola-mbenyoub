from utils.db_connection import get_db_connection

class DrapeauService:

    @staticmethod
    def add_drapeau(id_equipe: int, chemin_image: str) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO drapeau (id_equipe, chemin_image) VALUES (%s, %s)"
                cursor.execute(sql, (id_equipe, chemin_image))
                connection.commit()
                return True
        finally:
            connection.close()

    @staticmethod
    def delete_drapeau(id_drapeau: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")

        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM drapeau WHERE id_drapeau = %s"
                cursor.execute(sql, (id_drapeau,))
                connection.commit()
                return cursor.rowcount > 0
        finally:
            connection.close()

    @staticmethod
    def get_drapeau(id_drapeau: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM drapeau WHERE id_drapeau = %s"
                cursor.execute(sql, (id_drapeau,))
                return cursor.fetchone()
        finally:
            connection.close()

    @staticmethod
    def get_all_drapeaux() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM drapeau"
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            connection.close()
