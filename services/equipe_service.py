from utilsp.db_connection import get_db_connection

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

    @staticmethod
    def get_all_result_by_equipe(id_equipe) -> list[dict]:
        connection = get_db_connection()
        if not connection:
            return []
    
        try:
            with connection.cursor() as cursor:
                sql = """
                    SELECT 
    e.nom AS equipe,
    COUNT(r.id_match) AS nombre_de_matchs,
    COALESCE(SUM(
        CASE 
            WHEN r.id_equipe1 = e.id_equipe THEN res.buts_equipe1_temps_reglementaire
            ELSE res.buts_equipe2_temps_reglementaire
        END
    ), 0) AS buts_temps_reglementaire,
    COALESCE(SUM(
        CASE 
            WHEN r.id_equipe1 = e.id_equipe THEN res.buts_equipe1_apres_prolongation
            ELSE res.buts_equipe2_apres_prolongation
        END
    ), 0) AS buts_apres_prolongation,
    COALESCE(SUM(
        CASE 
            WHEN r.id_equipe1 = e.id_equipe THEN res.score_tirs_au_but_equipe1
            ELSE res.score_tirs_au_but_equipe2
        END
    ), 0) AS buts_tirs_au_but
FROM equipe e
LEFT JOIN rencontre r ON e.id_equipe = r.id_equipe1 OR e.id_equipe = r.id_equipe2
LEFT JOIN resultat res ON r.id_resultat = res.id_resultat
WHERE e.id_equipe = %s
GROUP BY e.nom;
                """
                cursor.execute(sql, (id_equipe,))
                return cursor.fetchall()
        except Exception as e:
            print(f"Erreur SQL: {str(e)}")
            return []
        finally:
            connection.close()