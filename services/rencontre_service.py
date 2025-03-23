from utils.db_connection import get_db_connection

class RencontreService:
    @staticmethod
    def add_rencontre(score_final, phase_tournoi, date, id_stade, id_equipe, id_equipe_equipeB) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = """
                INSERT INTO Rencontre (Score_Final, Phase_Tournoi, Date, Id_Stade, Id_Equipe, Id_Equipe_EquipeB) 
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (score_final, phase_tournoi, date, id_stade, id_equipe, id_equipe_equipeB))
                connection.commit()
                return True
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def delete_rencontre(id_match) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM Rencontre WHERE Id_Match = %s"
                cursor.execute(sql, (id_match,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def get_rencontre(id_match) -> dict | None:
        connection = get_db_connection()
        if not connection:
            return None
        try:
            with connection.cursor(dictionary=True) as cursor:
                sql = "SELECT * FROM Rencontre WHERE Id_Match = %s"
                cursor.execute(sql, (id_match,))
                rencontre = cursor.fetchone()
                return rencontre
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return None
        finally:
            connection.close()

    @staticmethod
    def get_all_rencontres() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            return []
        try:
            with connection.cursor(dictionary=True) as cursor:
                sql = "SELECT * FROM Rencontre"
                cursor.execute(sql)
                rencontres = cursor.fetchall()
                return rencontres
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return []
        finally:
            connection.close()
