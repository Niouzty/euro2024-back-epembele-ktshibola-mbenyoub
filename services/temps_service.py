from utils.db_connection import get_db_connection

class TempsService:

    @staticmethod
    def add_temps(date_heure_match: str) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO temps (date_heure_match) VALUES (%s)"
                cursor.execute(sql, (date_heure_match,))
                connection.commit()
                return True
        except Exception as e:
            print(f"Erreur lors de l'ajout du temps : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def delete_temps(id_temps: int) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM temps WHERE id_temps = %s"
                cursor.execute(sql, (id_temps,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Erreur lors de la suppression du temps : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def get_temps(id_temps: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            return None
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM temps WHERE id_temps = %s"
                cursor.execute(sql, (id_temps,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Erreur lors de la récupération du temps : {e}")
            return None
        finally:
            connection.close()

    @staticmethod
    def get_all_temps() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            return []
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM temps"
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print(f"Erreur lors de la récupération des temps : {e}")
            return []
        finally:
            connection.close()