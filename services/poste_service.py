from models.poste_model import Poste
from shared.db_connection import get_db_connection

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
    def get_poste(id_poste: int) -> Poste | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM poste WHERE id_poste = %s"
            cursor.execute(sql, (id_poste,))
            result = cursor.fetchone()
            return Poste(**result) if result else None

    @staticmethod
    def get_postes(offset: int, limit: int) -> list[Poste]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Échec de la connexion à la base de données.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM poste LIMIT %s OFFSET %s"
            cursor.execute(sql, (limit, offset))
            rows = cursor.fetchall()
            return [Poste(**row) for row in rows]

    @staticmethod
    def get_number_row() -> int:
        conn = get_db_connection()
        if not conn:
            raise ConnectionError("Connexion à la base de données échouée.")

        with conn.cursor() as cursor:
            query = "SELECT COUNT(*) FROM poste"
            cursor.execute(query)
            result = cursor.fetchone()
            return result['COUNT(*)'] if result else 0