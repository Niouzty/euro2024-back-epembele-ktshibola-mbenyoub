from flask import Blueprint, jsonify, request, Response
from services.groupe_service import GroupeService

groupe_controller = Blueprint('groupes', __name__, url_prefix='/groupes')

@groupe_controller.route('/', methods=['POST'])
def add_groupe() -> tuple[Response, int]:
    data = request.get_json()
    nom = data.get('nom')
    GroupeService.add_groupe(nom)
    return jsonify(data), 201

@groupe_controller.route('/<int:id_groupe>', methods=['DELETE'])
def delete_groupe(id_groupe) -> tuple[Response, int]:
    success = GroupeService.delete_groupe(id_groupe)
    if success:
        return jsonify({"message": "Le groupe a été supprimé avec succès."}), 200
    return jsonify({"message": "La suppression du groupe a échoué."}), 400

@groupe_controller.route('/<int:id_groupe>', methods=['GET'])
def get_groupe(id_groupe: int) -> tuple[Response, int]:
    groupe = GroupeService.get_groupe(id_groupe)
    if groupe:
        return jsonify(groupe), 200
    return jsonify({"message": "Groupe non trouvé."}), 404

@groupe_controller.route('/', methods=['GET'])
def get_all_groupes() -> tuple[Response, int]:
    groupes = GroupeService.get_all_groupes()
    if groupes:
        return jsonify(groupes), 200
    return jsonify({"message": "Aucun groupe trouvé."}), 404