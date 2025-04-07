from flask import Blueprint, jsonify
import utilsp.db_connection

database_controller = Blueprint("database", __name__, url_prefix='/database')

@database_controller.route("/", methods=["GET"])
def test_db():
    connection = None  
    try:
        connection = utilsp.db_connection.get_db_connection() 
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from equipe")
            result = cursor.fetchone()
        return jsonify({"message": "Connexion réussie ! 🚀 ", "result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection: 
            connection.close()
