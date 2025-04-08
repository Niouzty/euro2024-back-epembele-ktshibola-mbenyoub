from shared.db_connection import get_db_connection

class StatsJoueurService:

    @staticmethod
    def add_stats_joueur(buts_marques: int, passes_decisives: int, cartons_jaunes: int, cartons_rouges: int, minutes_jouees: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO stats_joueur (buts_marques, passes_decisives, cartons_jaunes, cartons_rouges, minutes_jouees)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (buts_marques, passes_decisives, cartons_jaunes, cartons_rouges, minutes_jouees))
            connection.commit()
            return True

    @staticmethod
    def delete_stats_joueur(id_stats_joueur: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor() as cursor:
            sql = "DELETE FROM stats_joueur WHERE id_stats_joueur = %s"
            cursor.execute(sql, (id_stats_joueur,))
            connection.commit()
            return cursor.rowcount > 0

    @staticmethod
    def get_stats_joueur(id_stats_joueur: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM stats_joueur WHERE id_stats_joueur = %s"
            cursor.execute(sql, (id_stats_joueur,))
            return cursor.fetchone()

    @staticmethod
    def get_all_stats_joueurs() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM stats_joueur"
            cursor.execute(sql)
            return cursor.fetchall()

    @staticmethod
    def get_top_butteurs() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base de données échouée.")
        with connection.cursor(dictionary=True) as cursor:
            sql = """
            SELECT * from joueur 
            JOIN stats_joueur USING(id_stats_joueur) 
            ORDER BY buts_marques DESC;
            """
            cursor.execute(sql)
            return cursor.fetchall()
