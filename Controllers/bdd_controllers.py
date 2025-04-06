from flask import Flask, request, jsonify, Blueprint

from Services.services_database import services_database

bdd_controllers = Blueprint('bdd_controllers', __name__, url_prefix='/bdd')

service_bdd = services_database()

@bdd_controllers.route('/schema')
def schema_db():
    tables = service_bdd.get_tables()
    tables_dict = [table.to_dict() for table in tables]

    return jsonify(tables_dict), 200

@bdd_controllers.route('/schema/<table>')
def schema_table(table: str):
    if not table or table == '':
        return jsonify({'error': "Table non definie"}),400

    table = service_bdd.get_table(table)

    return jsonify(table.to_dict()), 200