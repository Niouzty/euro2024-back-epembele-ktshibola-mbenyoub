from flask import Blueprint, jsonify, request, Response
from services.poste_service import PosteService

poste_controller = Blueprint('postes', __name__, url_prefix='/postes')

@poste_controller.route('/', methods=['POST'])
def add_poste() -> tuple[Response, int]:
    data = request.get_json()
    nom_poste = data.get('nom_poste')
    PosteService.add_poste(nom_poste)
    return jsonify(data), 201

@poste_controller.route('/<int:id_poste>', methods=['DELETE'])
def delete_poste(id_poste) -> tuple[Response, int]:
    success = PosteService.delete_poste(id_poste)
    if success:
        return jsonify({"message": "Le poste a été supprimé avec succès."}), 200
    return jsonify({"message": "La suppression du poste a échoué."}), 400

@poste_controller.route('/<int:id_poste>', methods=['GET'])
def get_poste(id_poste: int) -> tuple[Response, int]:
    poste = PosteService.get_poste(id_poste)
    if poste:
        return jsonify(poste), 200
    return jsonify({"message": "Poste non trouvé."}), 404

@poste_controller.route('/', methods=['GET'])
def get_all_postes() -> tuple[Response, int]:
    postes = PosteService.get_all_postes()
    if postes:
        return jsonify(postes), 200
    return jsonify({"message": "Aucun poste trouvé."}), 404