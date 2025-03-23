from utils.db_connection import get_db_connection

class ArbitreService:

    @staticmethod
    def add_arbitre(nom: str, prenom: str, id_nationalite: int) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO arbitre (nom, prenom, id_nationalite) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nom, prenom, id_nationalite))
                connection.commit()
                return True
        except Exception as e:
            print(f"Erreur lors de l'ajout de l'arbitre : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def delete_arbitre(id_arbitre: int) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM arbitre WHERE id_arbitre = %s"
                cursor.execute(sql, (id_arbitre,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Erreur lors de la suppression de l'arbitre : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def get_arbitre(id_arbitre: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            return None
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM arbitre WHERE id_arbitre = %s"
                cursor.execute(sql, (id_arbitre,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Erreur lors de la récupération de l'arbitre : {e}")
            return None
        finally:
            connection.close()

    @staticmethod
    def get_all_arbitres() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            return []
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM arbitre"
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print(f"Erreur lors de la récupération des arbitres : {e}")
            return []
        finally:
            connection.close()