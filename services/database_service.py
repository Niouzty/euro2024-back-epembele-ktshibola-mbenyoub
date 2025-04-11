from models.table_model import Table
from shared.db_connection import get_db_connection


class ServicesDatabase:

    @staticmethod
    def get_tables() -> list[Table]:
        connection = get_db_connection()

        if connection is None:
            raise ConnectionError("Connexion à la base de données échouée.")

        query = """
        SELECT TABLE_NAME, COLUMN_NAME 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_SCHEMA = 'euro2024';
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()

        tables_dict = {}
        for row in results:
            table_name, column_name = row['TABLE_NAME'], row['COLUMN_NAME']
            if table_name not in tables_dict:
                tables_dict[table_name] = []
            tables_dict[table_name].append(column_name)

        return [Table(name, cols) for name, cols in tables_dict.items()]

    @staticmethod
    def get_table(table_name: str) -> Table | None:
        connection = get_db_connection()

        if connection is None:
            raise ConnectionError("Connexion à la base de données échouée.")

        query = """
        SELECT COLUMN_NAME 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_SCHEMA = 'euro2024' AND TABLE_NAME = %s;
        """

        with connection.cursor() as cursor:
            cursor.execute(query, (table_name,))
            results = cursor.fetchall()

        if not results:
            return None

        colonnes = [row['COLUMN_NAME'] for row in results]
        return Table(table_name, colonnes)