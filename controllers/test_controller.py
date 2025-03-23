from flask import Blueprint, jsonify
from utils.db_connection import get_db_connection

test_controller = Blueprint("test", __name__, url_prefix='//test-db')

@test_controller.route("/", methods=["GET"])
def test_db():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from rencontre")
            result = cursor.fetchone()
        return jsonify({"message": "Connexion réussie ! 🚀 ", "result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()
