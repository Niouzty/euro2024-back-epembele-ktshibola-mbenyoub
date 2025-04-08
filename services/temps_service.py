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
    def get_temps(id_temps: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM temps WHERE id_temps = %s"
            cursor.execute(sql, (id_temps,))
            return cursor.fetchone()

    @staticmethod
    def get_all_temps() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM temps"
            cursor.execute(sql)
            return cursor.fetchall()
