from shared.db_connection import get_db_connection

class ArbitreService:

    @staticmethod
    def add_arbitre(nom: str, prenom: str, id_nationalite: int) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO arbitre (nom, prenom, id_nationalite) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nom, prenom, id_nationalite))
                connection.commit()
                return True
        except Exception as e:
            print(f"Erreur lors de l'ajout de l'arbitre : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def delete_arbitre(id_arbitre: int) -> bool:
        connection = get_db_connection()
        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM arbitre WHERE id_arbitre = %s"
                cursor.execute(sql, (id_arbitre,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Erreur lors de la suppression de l'arbitre : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def get_arbitre(id_arbitre: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            return None
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM arbitre WHERE id_arbitre = %s"
                cursor.execute(sql, (id_arbitre,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Erreur lors de la récupération de l'arbitre : {e}")
            return None
        finally:
            connection.close()

    @staticmethod
    def get_all_arbitres() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            return []
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM arbitre"
                cursor.execute(sql)
                arbitres = cursor.fetchall()
                return arbitres
        except Exception as e:
            print(f"Erreur lors de la récupération des arbitres : {e}")
            return []
        finally:
            connection.close()

    @staticmethod
    def get_all_result() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            return []
    
        try:
            with connection.cursor() as cursor:  
                sql = """
                    SELECT
                        a.id_arbitre
                        a.nom, 
                        a.prenom, 
                        COUNT(DISTINCT r.id_match) AS nombre_de_matchs,
                        COUNT(c.id_carton) AS nombre_de_cartons,
                        COALESCE(SUM(CASE WHEN c.type_carton = 'jaune' THEN 1 ELSE 0 END), 0) AS cartons_jaunes,
                        COALESCE(SUM(CASE WHEN c.type_carton = 'rouge' THEN 1 ELSE 0 END), 0) AS cartons_rouges
                    FROM arbitre a
                    LEFT JOIN rencontre r ON a.id_arbitre = r.id_arbitre
                    LEFT JOIN carton c ON r.id_match = c.id_match AND a.id_arbitre = c.id_arbitre
                    WHERE a.id_arbitre = %s
                    GROUP BY a.id_arbitre, a.nom, a.prenom;
                """
                cursor.execute(sql)  
                return cursor.fetchall() or [] 
        except Exception as e:
            print(f"Erreur lors de la récupération de l'arbitre : {e}")
            return []
        finally:
            connection.close()