from flask import Flask, jsonify, request, Blueprint

from Services.services_stades import StadeService
from Modeles import Stade

stade_controllers = Blueprint('stade_controllers', __name__, url_prefix='/stades')

services_stades = StadeService()


@stade_controllers.route('/', methods=['GET'])
def get_stades():
    page = int(request.args.get('offset', 1,int))  #
    taille_page = int(request.args.get('limit', 10,int))

    offset = (page - 1) * taille_page

    stades = services_stades.get_stades(offset, taille_page)

    return jsonify(stades), 200


@stade_controllers.route('/<int:stade_id>', methods=['GET'])
def get_stade(stade_id):
    stade = services_stades.get_stade(stade_id)
    if stade:
        return jsonify(stade), 200
    return jsonify({"error": "Stade non trouvé"}), 404


@stade_controllers.route('/', methods=['POST'])
def ajouter_stade():
    data = request.get_json()
    if not all(k in data for k in ("id_stade", "nom", "ville", "capacite")):
        return jsonify({"error": "Données invalides"}), 400

    stade = Stade(data["id_stade"], data["nom"], data["ville"], data["capacite"])
    services_stades.add_stade(stade)
    return jsonify({"message": "Stade ajouté avec succès"}), 201





@stade_controllers.route('/<int:stade_id>', methods=['DELETE'])
def supprimer_stade(stade_id):
    exist = services_stades.stade_exist(stade_id)
    if not exist:
        return jsonify({"error": "Stade non trouvé"}), 404

    services_stades.delete_stade(stade_id)
    return jsonify({"message": "Stade supprimé avec succès"}), 200



@stade_controllers.route('/nombres', methods=['GET'])
def get_nombres_stades():
    taille = services_stades.get_number_row()

    return jsonify({"result": taille}), 200


@stade_controllers.route('/visitors/lenght', methods=['GET'])
def get_visitors_stades_lenght():
    stade_taille = services_stades.get_stade_visitor()
    return jsonify({"result": stade_taille}), 200


@stade_controllers.route('/<int:stade_id>', methods=['PATCH'])
def update_stade(stade_id):
    data = request.json

    if not data:
        return jsonify({"error": "Aucune donnée fournie"}), 400

    column, value = data.get("column"), data.get("value")

    if not column or value is None:
        return jsonify({"error": "Champs manquant"}), 400

    valid_columns = {"nom", "ville", "capacite"}

    if column not in valid_columns:
        return jsonify({"error": f"Colonne '{column}' non autorisée"}), 400

    success = services_stades.update_stade(stade_id, column, value)

    if not success:
        return jsonify({"error": "Erreur lors de la mise à jour du stade"}), 500

    return jsonify({"message": "Stade mis à jour avec succès"}), 200


@stade_controllers.route('/batch', methods=['POST'])
def insert():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Aucune donnée fournie"}), 400

    stades = data.get("stades")

    if not isinstance(stades, list):
        return jsonify({"error": "Le champ 'stades' doit être une liste"}), 400

    failed_insert = services_stades.insert_stade(stades)
    success_count = len(stades) - len(failed_insert)

    if len(failed_insert) == 0:
        return jsonify({"result": f"{success_count} stades insérés"}), 200

    if len(failed_insert) < len(stades):
        return jsonify({
            "result": f"{success_count} stades insérés, {len(failed_insert)} erreurs",
            "error": failed_insert
        }), 207


    return jsonify({"error": f"0/{len(stades)} insert","rows":failed_insert}),400