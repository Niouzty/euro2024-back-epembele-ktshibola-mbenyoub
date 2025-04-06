from datetime import date
from Services.BD import BD
from Modeles.Stade import Stade
class StadeService:
    def __init__(self):
        self.conn = BD.get_connexion()
        self.cursor = BD.get_cursor()

        if self.conn is None:
            raise Exception("Erreur : Connexion à la base de données non établie.")
        else:
            print(self.conn)

        if self.cursor is None:
            raise Exception(" Erreur : Impossible d'obtenir un curseur de base de données.")
        else:
            print(self.cursor)



    def add_stade(self, stade: Stade):
        query = "insert into stade (id_stade, nom, ville, capacite) values (%s, %s, %s, %s)"
        values = (stade.id_stade, stade.nom, stade.ville, stade.capacite)
        try:

            self.cursor.execute(query, values)
            self.conn.commit()
        except Exception as e:
            print(f"Erreur lors de l'ajout du stade : {e}")
            self.conn.rollback()

    def delete_stade(self, id_stade: int):
        query = "delete from stade where id_stade = %s"
        try:
            self.cursor.execute(query, (id_stade,))
            self.conn.commit()
        except Exception as e:
            print(f"Erreur lor de la suppression du stade : {e}")
            self.conn.rollback()

    def get_stade(self, id_stade: int):
        query = "select * from stade where id_stade = %s"
        try:
            self.cursor.execute(query, (id_stade,))
            result = self.cursor.fetchone()
            return Stade(*result).to_dict() if result else None
        except Exception as e:
            print(f"Erreur lors de la récupération du stade : {e}")
            return None

    def get_stades(self, offset: int, limit: int):
        query = "SELECT * FROM stade LIMIT %s OFFSET %s"
        try:
            self.cursor.execute(query, (limit, offset))
            results = self.cursor.fetchall()

            stades = []
            for row in results:
                stades.append(Stade(row['Id_Stade'], row['Nom'], row['Ville'], row['Capacite']).to_dict())

            return {"result": stades}
        except Exception as e:
            print(f" Erreur lors de la récupération des stades : {e}")
            return {"result": []}

    def sort_by_capacity(self):
        query = "select * from stade order by capacite asc"
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return [Stade(*row).to_dict() for row in results]
        except Exception as e:
            print(f" Erreur lors du tri des stades : {e}")
            return []

    def stade_exist(self, stade_id):
        query = "select id_stade from stade where id_stade = %s"
        try:
            self.cursor.execute(query, (stade_id,))
            result = self.cursor.fetchone()
            return result is not None
        except Exception as e:
            print(f"Erreur lors de la vérification de l'existence du stade : {e}")
            return False

    def get_number_row(self):
        query = "SELECT COUNT(*) FROM stade"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            if result:
                return result['COUNT(*)']
            else:
                return 0
        except Exception as e:
            print(f"Erreur lors de la récupération du nombre de stades : {e}")
            return 0

    def get_stade_visitor(self):
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
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(f"Erreur lors de la récupération des données des stades : {e}")
            return []

    def update_stade(self, id_stade: int, column: str, value: str):

        query = f"UPDATE stade SET {column} = %s WHERE id_stade = %s"

        try:
            self.cursor.execute(query, (value, id_stade))
            self.conn.commit()

        except Exception as e:
            print(f"Erreur lors de la mise à jour du stade : {e}")
            self.conn.rollback()
            return False

        return True

    def get_rencontres(self, id_stade: int, type_match: int):


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

        try:
            self.cursor.execute(query, (id_stade, today.year, today.year, today.month, today.year, today.month, today.day))
            results = self.cursor.fetchall()
            return [Rencontre(*row).to_dict() for row in results]
        except Exception as e:
            print(f"Erreur lors de la récupération des rencontres : {e}")
            return []

    def insert_stade(self, data: list):
        non_inserees = []

        for row in data:
            try:
                id_stade = row.get('id_stade', 0)
                nom = row.get('nom')
                id_ville = row.get('id_ville')
                capacite = row.get('capacite')

                if id_stade > 0:
                    query = "INSERT INTO stade (id_stade, nom, id_ville, capacite) VALUES (%s, %s, %s, %s)"
                    values = (id_stade, nom, id_ville, capacite)
                else:
                    query = "INSERT INTO stade (nom, id_ville, capacite) VALUES (%s, %s, %s)"
                    values = (nom, id_ville, capacite)

                self.cursor.execute(query, values)

            except Exception as e:
                print(f"Erreur insertion ligne {row} → {e}")
                non_inserees.append(row)

        self.conn.commit()
        return non_inserees





