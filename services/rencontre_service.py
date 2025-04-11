
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
    def get_rencontres(offset: int, limit: int) -> list[Rencontre]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Échec de la connexion à la base de données.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM rencontre LIMIT %s OFFSET %s"
            cursor.execute(sql, (limit, offset))
            rows = cursor.fetchall()
            return [Rencontre(**row) for row in rows]

    @staticmethod
    def get_rencontre(id: int) -> Rencontre | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM rencontre where Id_match = %s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            return Rencontre(**result) if result else None

    @staticmethod
    def get_number_row() -> int:
        conn = get_db_connection()
        if not conn:
            raise ConnectionError("Connexion à la base de données échouée.")

        with conn.cursor() as cursor:
            query = "SELECT COUNT(*) FROM Rencontre"
            cursor.execute(query)
            result = cursor.fetchone()
            return result['COUNT(*)'] if result else 0


   