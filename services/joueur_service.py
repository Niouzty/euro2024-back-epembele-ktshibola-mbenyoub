from utils.db_connection import get_db_connection

class JoueurService:

    @staticmethod
    def add_joueur(nom: str, prenom: str, date_naissance: str, id_nationalite: int, id_poste: int, num_maillot: int, id_equipe: int) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = """
                INSERT INTO joueur (nom, prenom, date_naissance, id_nationalite, id_poste, num_maillot, id_equipe)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (nom, prenom, date_naissance, id_nationalite, id_poste, num_maillot, id_equipe))
                connection.commit()
                return True
        except Exception as e:
            print(f"Erreur lors de l'ajout du joueur : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def delete_joueur(id_joueur: int) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM joueur WHERE id_joueur = %s"
                cursor.execute(sql, (id_joueur,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Erreur lors de la suppression du joueur : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def get_joueur(id_joueur: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            return None
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM joueur WHERE id_joueur = %s"
                cursor.execute(sql, (id_joueur,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Erreur lors de la récupération du joueur : {e}")
            return None
        finally:
            connection.close()

    @staticmethod
    def get_all_joueurs() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            return []
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM joueur"
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print(f"Erreur lors de la récupération des joueurs : {e}")
            return []
        finally:
            connection.close()