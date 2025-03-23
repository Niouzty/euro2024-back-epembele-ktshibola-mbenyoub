from flask import Blueprint, jsonify, request, Response
from services.ville_service import VilleService

ville_controller = Blueprint('villes', __name__, url_prefix='/villes')

@ville_controller.route('/', methods=['POST'])
def add_ville() -> tuple[Response, int]:
    data = request.get_json()
    nom = data.get('nom')
    VilleService.add_ville(nom)
    return jsonify(data), 201

@ville_controller.route('/<int:id_ville>', methods=['DELETE'])
def delete_ville(id_ville) -> tuple[Response, int]:
    success = VilleService.delete_ville(id_ville)
    if success:
        return jsonify({"message": "La ville a été supprimée avec succès."}), 200
    return jsonify({"message": "La suppression de la ville a échoué."}), 400

@ville_controller.route('/<int:id_ville>', methods=['GET'])
def get_ville(id_ville: int) -> tuple[Response, int]:
    ville = VilleService.get_ville(id_ville)
    if ville:
        return jsonify(ville), 200
    return jsonify({"message": "Ville non trouvée."}), 404

@ville_controller.route('/', methods=['GET'])
def get_all_villes() -> tuple[Response, int]:
    villes = VilleService.get_all_villes()
    if villes:
        return jsonify(villes), 200
    return jsonify({"message": "Aucune ville trouvée."}), 404