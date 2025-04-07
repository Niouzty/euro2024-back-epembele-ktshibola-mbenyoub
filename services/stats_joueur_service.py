from shared.db_connection import get_db_connection

class StatsJoueurService:

    @staticmethod
    def add_stats_joueur(buts_marques: int, passes_decisives: int, cartons_jaunes: int, cartons_rouges: int, minutes_jouees: int) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = """
                INSERT INTO stats_joueur (buts_marques, passes_decisives, cartons_jaunes, cartons_rouges, minutes_jouees)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (buts_marques, passes_decisives, cartons_jaunes, cartons_rouges, minutes_jouees))
                connection.commit()
                return True
        except Exception as e:
            print(f"Erreur lors de l'ajout des statistiques du joueur : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def delete_stats_joueur(id_stats_joueur: int) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM stats_joueur WHERE id_stats_joueur = %s"
                cursor.execute(sql, (id_stats_joueur,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Erreur lors de la suppression des statistiques du joueur : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def get_stats_joueur(id_stats_joueur: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            return None
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM stats_joueur WHERE id_stats_joueur = %s"
                cursor.execute(sql, (id_stats_joueur,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Erreur lors de la récupération des statistiques du joueur : {e}")
            return None
        finally:
            connection.close()

    @staticmethod
    def get_all_stats_joueurs() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            return []
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM stats_joueur"
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print(f"Erreur lors de la récupération des statistiques des joueurs : {e}")
            return []
        finally:
            connection.close()

    @staticmethod
    def get_top_butteurs() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            return[]
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * from joueur join stats_joueur using(id_stats_joueur) ORDER by buts_marques desc;"
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print(f"Erreur lors de la récupération des joueurs : {e}")
            return[]
        finally:
            connection.close()