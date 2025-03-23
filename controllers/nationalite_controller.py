from flask import Blueprint, jsonify, request, Response
from services.nationalite_service import NationaliteService

nationalite_controller = Blueprint('nationalites', __name__, url_prefix='/nationalites')

@nationalite_controller.route('/', methods=['POST'])
def add_nationalite() -> tuple[Response, int]:
    data = request.get_json()
    nom = data.get('nom')
    NationaliteService.add_nationalite(nom)
    return jsonify(data), 201

@nationalite_controller.route('/<int:id_nationalite>', methods=['DELETE'])
def delete_nationalite(id_nationalite) -> tuple[Response, int]:
    success = NationaliteService.delete_nationalite(id_nationalite)
    if success:
        return jsonify({"message": "La nationalité a été supprimée avec succès."}), 200
    return jsonify({"message": "La suppression de la nationalité a échoué."}), 400

@nationalite_controller.route('/<int:id_nationalite>', methods=['GET'])
def get_nationalite(id_nationalite: int) -> tuple[Response, int]:
    nationalite = NationaliteService.get_nationalite(id_nationalite)
    if nationalite:
        return jsonify(nationalite), 200
    return jsonify({"message": "Nationalité non trouvée."}), 404

@nationalite_controller.route('/', methods=['GET'])
def get_all_nationalites() -> tuple[Response, int]:
    nationalites = NationaliteService.get_all_nationalites()
    if nationalites:
        return jsonify(nationalites), 200
    return jsonify({"message": "Aucune nationalité trouvée."}), 404