from flask import Blueprint, jsonify, request, Response
from services.drapeau_service import DrapeauService

drapeau_controller = Blueprint('drapeaux', __name__, url_prefix='/drapeaux')

@drapeau_controller.route('/', methods=['POST'])
def add_drapeau() -> tuple[Response, int]:
    data = request.get_json()
    id_equipe = data.get('id_equipe')
    chemin_image = data.get('chemin_image')
    DrapeauService.add_drapeau(id_equipe, chemin_image)
    return jsonify(data), 201

@drapeau_controller.route('/<int:id_drapeau>', methods=['DELETE'])
def delete_drapeau(id_drapeau) -> tuple[Response, int]:
    success = DrapeauService.delete_drapeau(id_drapeau)
    if success:
        return jsonify({"message": "Le drapeau a été supprimé avec succès."}), 200
    return jsonify({"message": "La suppression du drapeau a échoué."}), 400

@drapeau_controller.route('/<int:id_drapeau>', methods=['GET'])
def get_drapeau(id_drapeau: int) -> tuple[Response, int]:
    drapeau = DrapeauService.get_drapeau(id_drapeau)
    if drapeau:
        return jsonify(drapeau), 200
    return jsonify({"message": "Drapeau non trouvé."}), 404

@drapeau_controller.route('/', methods=['GET'])
def get_all_drapeaux() -> tuple[Response, int]:
    drapeaux = DrapeauService.get_all_drapeaux()
    if drapeaux:
        return jsonify(drapeaux), 200
    return jsonify({"message": "Aucun drapeau trouvé."}), 404