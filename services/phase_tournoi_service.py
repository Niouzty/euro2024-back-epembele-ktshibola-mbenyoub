from utils.db_connection import get_db_connection

class PhaseTournoiService:

    @staticmethod
    def add_phase_tournoi(nom: str) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO phase_tournoi (nom) VALUES (%s)"
                cursor.execute(sql, (nom,))
                connection.commit()
                return True
        except Exception as e:
            print(f"Erreur lors de l'ajout de la phase du tournoi : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def delete_phase_tournoi(id_phase: int) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM phase_tournoi WHERE id_phase = %s"
                cursor.execute(sql, (id_phase,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Erreur lors de la suppression de la phase du tournoi : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def get_phase_tournoi(id_phase: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            return None
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM phase_tournoi WHERE id_phase = %s"
                cursor.execute(sql, (id_phase,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Erreur lors de la récupération de la phase du tournoi : {e}")
            return None
        finally:
            connection.close()

    @staticmethod
    def get_all_phases_tournoi() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            return []
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM phase_tournoi"
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print(f"Erreur lors de la récupération des phases du tournoi : {e}")
            return []
        finally:
            connection.close()