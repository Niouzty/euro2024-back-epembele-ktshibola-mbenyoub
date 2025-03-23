import mysql.connector

class BD:
    _connexion = None
    _cursor = None

    @staticmethod
    def init_bd():
        """Initialise la connexion à la base de données."""
        try:
            if BD._connexion is None or not BD._connexion.is_connected():
                BD._connexion = mysql.connector.connect(
                    user='root',
                    password='',
                    host='localhost',
                    database='bd_euro_2024'
                )
                BD._cursor = BD._connexion.cursor(dictionary=True)

        except mysql.connector.Error as err:
            print(f"❌ Erreur de connexion à la BDD : {err}")
            BD._connexion = None
            BD._cursor = None

    @staticmethod
    def get_connexion():
        """Retourne la connexion à la base de données."""
        if BD._connexion is None or not BD._connexion.is_connected():
            BD.init_bd()
        return BD._connexion

    @staticmethod
    def get_cursor():
        """Retourne le curseur de la base de données."""
        if BD._cursor is None:
            BD.init_bd()
        return BD._cursor

    @staticmethod
    def close_connexion():
        """Ferme la connexion proprement."""
        if BD._cursor:
            BD._cursor.close()
            BD._cursor = None
        if BD._connexion:
            BD._connexion.close()
            BD ._connexion = None


