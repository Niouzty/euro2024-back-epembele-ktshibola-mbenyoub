from models.temps_model import Temps
from shared.db_connection import get_db_connection

class TempsService:

    @staticmethod
    def add_temps(date_heure_match: str) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "INSERT INTO temps (date_heure_match) VALUES (%s)"
            cursor.execute(sql, (date_heure_match,))
            connection.commit()
            return True

    @staticmethod
    def delete_temps(id_temps: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "DELETE FROM temps WHERE id_temps = %s"
            cursor.execute(sql, (id_temps,))
            connection.commit()
            return cursor.rowcount > 0

    @staticmethod
    def get_temps(id_temps: int) -> Temps | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM temps WHERE id_temps = %s"
            cursor.execute(sql, (id_temps,))
            result = cursor.fetchone()
            return Temps(**result) if result else None

    @staticmethod
    def get_tempss(offset: int, limit: int) -> list[Temps]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Échec de la connexion à la base de données.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM temps LIMIT %s OFFSET %s"
            cursor.execute(sql, (limit, offset))
            rows = cursor.fetchall()
            print(rows)
            return [Temps(**row) for row in rows]
    @staticmethod
    def get_number_row() -> int:
        conn = get_db_connection()
        if not conn:
            raise ConnectionError("Connexion à la base de données échouée.")

        with conn.cursor() as cursor:
            query = "SELECT COUNT(*) FROM temps"
            cursor.execute(query)
            result = cursor.fetchone()
            return result['COUNT(*)'] if result else 0