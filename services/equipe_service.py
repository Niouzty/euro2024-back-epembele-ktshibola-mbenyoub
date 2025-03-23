from utils.db_connection import get_db_connection

class EquipeService:

    @staticmethod
    def add_equipe(nom: str, groupe: str, entraineur: str) -> bool:
        connection = get_db_connection()

        if not connection:
            return False
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO equipe (nom, groupe, entraineur) values (%s, %s, %s)"
                cursor.execute(sql, (nom, groupe, entraineur))
                connection.commit()
                return True
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return False
        finally:
            connection.close()
            
    @staticmethod
    def delete_equipe(id_equipe: int) -> bool:
        connection = get_db_connection()

        if not connection:
            return False 
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM equipe WHERE id_equipe = %s"
                cursor.execute(sql, (id_equipe,))
                connection.commit()
                return cursor.rowcount > 0  
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def get_equipe(id_equipe: int) -> dict | None:
        connection = get_db_connection()

        if not connection:
            return None
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM equipe WHERE id_equipe = %s"
                cursor.execute(sql, (id_equipe,))
                connection.commit()
                return cursor.fetchone()
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return None
        finally:
            connection.close()
    
    @staticmethod
    def get_all_equipes() -> list[dict]:
        connection = get_db_connection()

        if not connection:
            return []  
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM equipe"
                cursor.execute(sql)
                equipes = cursor.fetchall()
                return equipes 
        except Exception as e:
            print(f" Erreur lors de la récupération des équipes : {e}")
            return []  
        finally:
            connection.close()  


    @staticmethod
    def get_equipes_by_groupe(id_groupe: str) -> list[dict]:
    
        connection = get_db_connection()
        if not connection:
            return [] 
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM equipe WHERE groupe = %s"
                cursor.execute(sql, (id_groupe,))
                equipes = cursor.fetchall()
                return equipes
        except Exception as e:
            print(f"Erreur lors de la récupération des équipes du groupe {id_groupe} : {e}")
            return [] 
        finally:
            connection.close()  