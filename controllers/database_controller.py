from flask import Blueprint, jsonify

from services.database_service import ServicesDatabase

database_bp = Blueprint('database_controller', __name__)


@database_bp.route("/tables", methods=["GET"])
def get_tables():
    try:
        tables = ServicesDatabase.get_tables()

        return jsonify(tables), 200

    except ConnectionError as e:
        return jsonify({"Erreur": str(e)}), 500


@database_bp.route("/tables/<string:table_name>", methods=["GET"])
def get_table(table_name):
    try:
        table = ServicesDatabase.get_table(table_name)
        if table is None:
            return jsonify({"Erreur": f"Table '{table_name}' introuvable."}), 404

        return jsonify(table), 200

    except ConnectionError as e:
        return jsonify({"Erreur": str(e)}), 500
