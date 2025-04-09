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
    def get_all_temps() -> list[Temps]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM temps"
            cursor.execute(sql)
            result = cursor.fetchall()
            return [Temps(**row) for row in result]