from shared.db_connection import get_db_connection

class ArbitreService:

    @staticmethod
    def add_arbitre(nom: str, prenom: str, id_nationalite: int) -> bool:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base échouée.")
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO arbitre (nom, prenom, id_nationalite) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nom, prenom, id_nationalite))
                connection.commit()
                return True
        finally:
            connection.close()

    @staticmethod
    def delete_arbitre(id_arbitre: int) -> int:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base échouée.")
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM arbitre WHERE id_arbitre = %s"
                cursor.execute(sql, (id_arbitre,))
                connection.commit()
                return cursor.rowcount
        finally:
            connection.close()

    @staticmethod
    def get_arbitre(id_arbitre: int) -> dict | None:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base échouée.")
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM arbitre WHERE id_arbitre = %s"
                cursor.execute(sql, (id_arbitre,))
                return cursor.fetchone()
        finally:
            connection.close()

    @staticmethod
    def get_all_arbitres() -> list[dict]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base échouée.")
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM arbitre"
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            connection.close()

    @staticmethod
    def get_all_result_by_id(id_arbitre: int) -> list[dict]:
        connection = get_db_connection()
        if not connection:
            raise ConnectionError("Connexion à la base échouée.")
        try:
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
                    WHERE a.id_arbitre = %s
                    GROUP BY a.id_arbitre, a.nom, a.prenom;
                """
                cursor.execute(sql, (id_arbitre,))
                return cursor.fetchall()
        finally:
            connection.close()
