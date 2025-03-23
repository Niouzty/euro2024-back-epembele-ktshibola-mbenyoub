from utils.db_connection import get_db_connection

class PosteService:

    @staticmethod
    def add_poste(nom_poste: str) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO poste (nom_poste) VALUES (%s)"
                cursor.execute(sql, (nom_poste,))
                connection.commit()
                return True
        except Exception as e:
            print(f"Erreur lors de l'ajout du poste : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def delete_poste(id_poste: int) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM poste WHERE id_poste = %s"
                cursor.execute(sql, (id_poste,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Erreur lors de la suppression du poste : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def get_poste(id_poste: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            return None
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM poste WHERE id_poste = %s"
                cursor.execute(sql, (id_poste,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Erreur lors de la récupération du poste : {e}")
            return None
        finally:
            connection.close()

    @staticmethod
    def get_all_postes() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            return []
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM poste"
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print(f"Erreur lors de la récupération des postes : {e}")
            return []
        finally:
            connection.close()