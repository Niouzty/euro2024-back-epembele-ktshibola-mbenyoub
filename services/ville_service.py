from shared.db_connection import get_db_connection

class VilleService:

    @staticmethod
    def add_ville(nom: str) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO ville (nom) VALUES (%s)"
                cursor.execute(sql, (nom,))
                connection.commit()
                return True
        except Exception as e:
            print(f"Erreur lors de l'ajout de la ville : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def delete_ville(id_ville: int) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM ville WHERE id_ville = %s"
                cursor.execute(sql, (id_ville,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Erreur lors de la suppression de la ville : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def get_ville(id_ville: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            return None
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM ville WHERE id_ville = %s"
                cursor.execute(sql, (id_ville,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Erreur lors de la récupération de la ville : {e}")
            return None
        finally:
            connection.close()

    @staticmethod
    def get_all_villes() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            return []
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM ville"
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print(f"Erreur lors de la récupération des villes : {e}")
            return []
        finally:
            connection.close()

    @staticmethod
    def update_ville(id_ville: int, new_nom: str) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE ville SET nom = %s WHERE id_ville = %s"
                cursor.execute(sql, (new_nom, id_ville))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Erreur lors de la mise à jour de la ville : {e}")
            return False
        finally:
            connection.close()