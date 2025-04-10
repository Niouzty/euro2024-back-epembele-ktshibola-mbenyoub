from datetime import date

from models.rencontre_model import Rencontre
from models.stade_model import Stade
from shared.db_connection import get_db_connection

class StadeService:

    @staticmethod
    def get_connexion():
        connection = get_db_connection()
        if connection is None:
            raise Exception("Erreur : Impossible d'obtenir une connexion à la base de données.")
        return connection

    @staticmethod
    def add_stade(nom: str, id_ville: int, capacite: int, id_stade: int = -1):
        conn = StadeService.get_connexion()
        with conn.cursor() as cursor:
            if id_stade > 0:
                query = "INSERT INTO stade (id_stade, nom, id_ville, capacite) VALUES (%s, %s, %s, %s)"
                values = (id_stade, nom, id_ville, capacite)
            else:
                query = "INSERT INTO stade (nom, id_ville, capacite) VALUES (%s, %s, %s)"
                values = (nom, id_ville, capacite)
            cursor.execute(query, values)
        conn.commit()
        return True

    @staticmethod
    def delete_stade(id_stade: int):
        conn = StadeService.get_connexion()
        if not conn:
            raise ConnectionError("erreur co bd")

        with conn.cursor() as cursor:
            query = "DELETE FROM stade WHERE id_stade = %s"
            cursor.execute(query, (id_stade,))
            conn.commit()
            return True

    @staticmethod
    def get_stade(id_stade: int):
        conn = StadeService.get_connexion()
        with conn.cursor() as cursor:
            query = "SELECT * FROM stade WHERE id_stade = %s"
            cursor.execute(query, (id_stade,))
            result = cursor.fetchone()
            if result:
                return Stade(**result)
            return None

    @staticmethod
    def get_stades(offset: int, limit: int):
        conn = StadeService.get_connexion()

        if not conn:
            raise ConnectionError("Connexion à la base de données échouée.")

        with conn.cursor() as cursor:
            query = "SELECT * FROM stade LIMIT %s OFFSET %s;"
            cursor.execute(query, (limit, offset))
            results = cursor.fetchall()
            return [Stade(**row) for row in results]


    @staticmethod
    def sort_by_capacity():
        conn = StadeService.get_connexion()
        with conn.cursor() as cursor:
            query = "SELECT * FROM stade ORDER BY capacite ASC"
            cursor.execute(query)
            results = cursor.fetchall()
            return [Stade(**row) for row in results]

    @staticmethod
    def stade_exist(stade_id: int) -> bool:
        conn = StadeService.get_connexion()
        with conn.cursor() as cursor:
            query = "SELECT id_stade FROM stade WHERE id_stade = %s"
            cursor.execute(query, (stade_id,))
            result = cursor.fetchone()
            return True if result else False

    @staticmethod
    def get_number_row() -> int:
        conn = StadeService.get_connexion()
        with conn.cursor() as cursor:
            query = "SELECT COUNT(*) FROM stade"
            cursor.execute(query)
            result = cursor.fetchone()
            return result['COUNT(*)'] if result else 0

    @staticmethod
    def get_stade_visitor():
        conn = StadeService.get_connexion()
        with conn.cursor() as cursor:
            query = """
                SELECT 
                    S.Nom AS stade, 
                    AVG(Match_Visiteurs.Visiteurs_Par_Match) AS avg_visitor
                FROM 
                    Stade S
                JOIN 
                    (
                        SELECT 
                            R.Id_Stade, 
                            R.Id_Match, 
                            COUNT(A.Id_Spec) AS Visiteurs_Par_Match
                        FROM 
                            Rencontre R
                        JOIN 
                            Assister A ON R.Id_Match = A.Id_Match
                        GROUP BY 
                            R.Id_Stade, R.Id_Match
                    ) AS Match_Visiteurs
                ON S.Id_Stade = Match_Visiteurs.Id_Stade
                GROUP BY 
                    S.Nom;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            return results

    @staticmethod
    def update_stade(id_stade: int, column: str, value: str) -> bool:
        conn = StadeService.get_connexion()
        with conn.cursor() as cursor:
            query = f"UPDATE stade SET {column} = %s WHERE id_stade = %s"
            cursor.execute(query, (value, id_stade))
            conn.commit()
            return True

    @staticmethod
    def get_rencontres(id_stade: int, type_match: int) -> list[Rencontre]:
        conn = StadeService.get_connexion()
        with conn.cursor() as cursor:
            today = date.today()
            query = """
                SELECT r.id_match, t.jour, t.mois, t.annee, e1.nom AS equipe1, e2.nom AS equipe2, s.nom AS stade, r.nb_spectateurs
                FROM rencontre r
                JOIN temps t ON r.id_temps = t.id_temps
                JOIN equipe e1 ON r.id_equipe1 = e1.id_equipe
                JOIN equipe e2 ON r.id_equipe2 = e2.id_equipe
                JOIN stade s ON r.id_stade = s.id_stade
                WHERE r.id_stade = %s
            """
            if type_match == 1:
                query += " AND (t.annee < %s OR (t.annee = %s AND t.mois < %s) OR (t.annee = %s AND t.mois = %s AND t.jour < %s))"
            elif type_match == 2:
                query += " AND (t.annee > %s OR (t.annee = %s AND t.mois > %s) OR (t.annee = %s AND t.mois = %s AND t.jour >= %s))"
            else:
                return {"error": "Type de match invalide"}

            cursor.execute(query, (id_stade, today.year, today.year, today.month, today.year, today.month, today.day))
            results = cursor.fetchall()
            return [Rencontre(*row).to_dict() for row in results]

