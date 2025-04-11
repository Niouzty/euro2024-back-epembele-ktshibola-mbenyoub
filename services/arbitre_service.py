from typing import List
from models.arbitre_model import Arbitre
from shared.db_connection import get_db_connection


class ArbitreService:

    @staticmethod
    def add_arbitre(nom: str, prenom: str, id_nationalite: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Échec de la connexion à la base de données.")
        with connection.cursor() as cursor:
            sql = "INSERT INTO arbitre (nom, prenom, id_nationalite) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nom, prenom, id_nationalite))
            connection.commit()
            return True

    @staticmethod
    def delete_arbitre(id_arbitre: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Échec de la connexion à la base de données.")
        with connection.cursor() as cursor:
            sql = "DELETE FROM arbitre WHERE id_arbitre = %s"
            cursor.execute(sql, (id_arbitre,))
            connection.commit()
            return cursor.rowcount > 0

    @staticmethod
    def get_arbitre(id_arbitre: int) -> Arbitre | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Échec de la connexion à la base de données.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM arbitre WHERE id_arbitre = %s"
            cursor.execute(sql, (id_arbitre,))
            row = cursor.fetchone()
            return Arbitre(**row) if row else None

    @staticmethod
    def get_arbitres(offset: int, limit: int) -> List[Arbitre]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Échec de la connexion à la base de données.")
        with connection.cursor() as cursor:
            sql = "SELECT * FROM arbitre LIMIT %s OFFSET %s"
            cursor.execute(sql, (limit, offset))
            rows = cursor.fetchall()
            return [Arbitre(**row) for row in rows]

    @staticmethod
    def get_number_row() -> int:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Échec de la connexion à la base de données.")
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(*) FROM arbitre"
            cursor.execute(sql)
            row = cursor.fetchone()
            return row['COUNT(*)'] if row else 0

    @staticmethod
    def get_all_result() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Échec de la connexion à la base de données.")
        with connection.cursor() as cursor:
            sql = """
                SELECT
                    a.id_arbitre,
                    a.nom, 
                    a.prenom, 
                    COUNT(DISTINCT r.id_match) AS nombre_de_matchs,
                    COUNT(c.id_carton) AS nombre_de_cartons,
                    COALESCE(SUM(CASE WHEN c.type_carton = 'jaune' THEN 1 ELSE 0 END), 0) AS cartons_jaunes,
                    COALESCE(SUM(CASE WHEN c.type_carton = 'rouge' THEN 1 ELSE 0 END), 0) AS cartons_rouges
                FROM arbitre a
                LEFT JOIN rencontre r ON a.id_arbitre = r.id_arbitre
                LEFT JOIN carton c ON r.id_match = c.id_match AND a.id_arbitre = c.id_arbitre
                GROUP BY a.id_arbitre, a.nom, a.prenom;
            """
            cursor.execute(sql)
            return cursor.fetchall()
