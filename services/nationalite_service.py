from utilsp.db_connection import get_db_connection

class NationaliteService:

    @staticmethod
    def add_nationalite(nom: str) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO nationalite (nom) VALUES (%s)"
                cursor.execute(sql, (nom,))
                connection.commit()
                return True
        except Exception as e:
            print(f"Erreur lors de l'ajout de la nationalité : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def delete_nationalite(id_nationalite: int) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM nationalite WHERE id_nationalite = %s"
                cursor.execute(sql, (id_nationalite,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Erreur lors de la suppression de la nationalité : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def get_nationalite(id_nationalite: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            return None
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM nationalite WHERE id_nationalite = %s"
                cursor.execute(sql, (id_nationalite,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Erreur lors de la récupération de la nationalité : {e}")
            return None
        finally:
            connection.close()

    @staticmethod
    def get_all_nationalites() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            return []
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM nationalite"
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print(f"Erreur lors de la récupération des nationalités : {e}")
            return []
        finally:
            connection.close()