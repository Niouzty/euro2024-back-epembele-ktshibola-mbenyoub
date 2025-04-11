from typing import List

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
    def get_phase_tournois(offset: int, limit: int) -> list[PhaseTournoi]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Échec de la connexion à la base de données.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM phase_tournoi LIMIT %s OFFSET %s"
            cursor.execute(sql, (limit, offset))
            rows = cursor.fetchall()
            return [PhaseTournoi(**row) for row in rows]

    @staticmethod
    def get_number_row() -> int:
        conn = get_db_connection()
        if not conn:
            raise ConnectionError("Connexion à la base de données échouée.")

        with conn.cursor() as cursor:
            query = "SELECT COUNT(*) FROM phase_tournoi"
            cursor.execute(query)
            result = cursor.fetchone()
            return result['COUNT(*)'] if result else 0