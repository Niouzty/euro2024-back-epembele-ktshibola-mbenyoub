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
