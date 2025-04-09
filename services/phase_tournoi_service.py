from models.phase_tournoi_model import PhaseTournoi
from shared.db_connection import get_db_connection

class PhaseTournoiService:

    @staticmethod
    def add_phase_tournoi(nom: str) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "INSERT INTO phase_tournoi (nom) VALUES (%s)"
            cursor.execute(sql, (nom,))
            connection.commit()
            return True

    @staticmethod
    def delete_phase_tournoi(id_phase: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "DELETE FROM phase_tournoi WHERE id_phase = %s"
            cursor.execute(sql, (id_phase,))
            connection.commit()
            return cursor.rowcount > 0

    @staticmethod
    def get_phase_tournoi(id_phase: int) -> PhaseTournoi | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM phase_tournoi WHERE id_phase = %s"
            cursor.execute(sql, (id_phase,))
            result = cursor.fetchone()
            return PhaseTournoi(**result) if result else None

    @staticmethod
    def get_all_phases_tournoi() -> list[PhaseTournoi]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM phase_tournoi"
            cursor.execute(sql)
            result = cursor.fetchall()
            return [PhaseTournoi(**row) for row in result]