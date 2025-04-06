import mysql

from Modeles.Table import Table
from Services.BD import BD


class services_database:

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

    def get_tables(self):
        query = """
        SELECT TABLE_NAME, COLUMN_NAME 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_SCHEMA = 'bd_euro_2024';
        """

        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()

            tables_dict = {}
            for row in results:
                table_name, column_name = row['TABLE_NAME'], row['COLUMN_NAME']
                print(row)
                if table_name not in tables_dict:
                    tables_dict[table_name] = []
                tables_dict[table_name].append(column_name)

            return [Table(name, cols) for name, cols in tables_dict.items()]

        except mysql.connector.Error as e:
            print(f"Erreur MySQL : {e}")
            return []



    def get_table(self,table_name):
        query = """
        SELECT TABLE_NAME, COLUMN_NAME 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_SCHEMA = 'bd_euro_2024' and TABLE_NAME = %s;
        """

        try:
            self.cursor.execute(query, (table_name,))
            results = self.cursor.fetchall()

            tables_dict = None
            table_name, column_name = row['TABLE_NAME'], row['COLUMN_NAME']

            tables_dict[table_name].append(column_name)

            return

        except mysql.connector.Error as e:
            print(f"Erreur MySQL : {e}")
            return []
