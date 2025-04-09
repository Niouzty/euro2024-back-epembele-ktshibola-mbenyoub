from typing import List

from models.resultat_model import Resultat
from shared.db_connection import get_db_connection

class ResultatService:

    @staticmethod
    def add_resultat(buts_equipe1: int, buts_equipe2: int, prolongation: bool, tirs_au_but: bool, buts_equipe1_prolongation: int, buts_equipe2_prolongation: int, score_tirs_equipe1: int, score_tirs_equipe2: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO resultat (buts_equipe1_temps_reglementaire, buts_equipe2_temps_reglementaire, prolongation, tirs_au_but, buts_equipe1_apres_prolongation, buts_equipe2_apres_prolongation, score_tirs_au_but_equipe1, score_tirs_au_but_equipe2)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (buts_equipe1, buts_equipe2, prolongation, tirs_au_but, buts_equipe1_prolongation, buts_equipe2_prolongation, score_tirs_equipe1, score_tirs_equipe2))
            connection.commit()
            return True

    @staticmethod
    def delete_resultat(id_resultat: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "DELETE FROM resultat WHERE id_resultat = %s"
            cursor.execute(sql, (id_resultat,))
            connection.commit()
            return cursor.rowcount > 0

    @staticmethod
    def get_resultat(id_resultat: int) -> Resultat | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM resultat WHERE id_resultat = %s"
            cursor.execute(sql, (id_resultat,))
            result =  cursor.fetchone()
            return Resultat(**result) if result else None

    @staticmethod
    def get_all_resultats() -> list[Resultat]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM resultat"
            cursor.execute(sql)
            result = cursor.fetchall()
            return [Resultat(**row) for row in result]