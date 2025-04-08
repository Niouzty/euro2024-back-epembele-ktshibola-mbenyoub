from utils.db_connection import get_db_connection

from models.drapeau_model import Drapeau


class DrapeauService:

    @staticmethod
    def add_drapeau(id_equipe: int, chemin_image: str) -> Drapeau:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")

        with connection.cursor() as cursor:
            sql = "INSERT INTO drapeau (id_equipe, chemin_image) VALUES (%s, %s) RETURNING id_drapeau"
            cursor.execute(sql, (id_equipe, chemin_image))
            id_drapeau = cursor.fetchone()[0]
            connection.commit()
            return Drapeau(id_drapeau, id_equipe, chemin_image)

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
                return Drapeau(*row)
            return None

    @staticmethod
    def get_all_drapeaux() -> list[Drapeau]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")

        with connection.cursor() as cursor:
            sql = "SELECT id_drapeau, id_equipe, chemin_image FROM drapeau"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [Drapeau(*row) for row in rows]