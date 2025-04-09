from models.rencontre_model import Rencontre
from shared.db_connection import get_db_connection

class RencontreService:

    @staticmethod
    def add_rencontre(score_final, phase_tournoi, date, id_stade, id_equipe, id_equipe_equipeB) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO Rencontre (Score_Final, Phase_Tournoi, Date, Id_Stade, Id_Equipe, Id_Equipe_EquipeB) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (score_final, phase_tournoi, date, id_stade, id_equipe, id_equipe_equipeB))
            connection.commit()
            return True

    @staticmethod
    def delete_rencontre(id_match) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "DELETE FROM Rencontre WHERE Id_Match = %s"
            cursor.execute(sql, (id_match,))
            connection.commit()
            return cursor.rowcount > 0

    @staticmethod
    def get_rencontre(id_match) -> Rencontre | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM Rencontre WHERE Id_Match = %s"
            cursor.execute(sql, (id_match,))
            result = cursor.fetchone()
            return Rencontre(**result) if result else None

    @staticmethod
    def get_all_rencontres() -> list[Rencontre]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM Rencontre"
            cursor.execute(sql)
            result = cursor.fetchall()
            return [Rencontre(**row) for row in result]