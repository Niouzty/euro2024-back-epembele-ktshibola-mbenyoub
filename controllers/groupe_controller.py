from flask import Blueprint, jsonify, request, Response
from services.groupe_service import GroupeService

groupe_controller = Blueprint('groupes', __name__, url_prefix='/groupes')


# Route pour ajouter un groupe
@groupe_controller.route('/', methods=['POST'])
def add_groupe() -> tuple[Response, int]:
    try:
        data = request.get_json()
        nom = data.get('nom')
        if not nom:
            return jsonify({"error": "Le nom du groupe est requis."}), 400

        GroupeService.add_groupe(nom)
        return jsonify(data), 201
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de l'ajout du groupe. {e}"}), 500


# Route pour supprimer un groupe
@groupe_controller.route('/<int:id_groupe>', methods=['DELETE'])
def delete_groupe(id_groupe) -> tuple[Response, int]:
    try:
        success = GroupeService.delete_groupe(id_groupe)
        if success:
            return jsonify({"message": "Le groupe a été supprimé avec succès."}), 200
        return jsonify({"error": f"La suppression du groupe a échoué. Le groupe n'existe peut-être pas."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la suppression du groupe. {e}"}), 500


# Route pour récupérer un groupe par ID
@groupe_controller.route('/<int:id_groupe>', methods=['GET'])
def get_groupe(id_groupe: int) -> tuple[Response, int]:
    try:
        groupe = GroupeService.get_groupe(id_groupe)
        if groupe:
            return jsonify(groupe), 200
        return jsonify({"error": "Groupe non trouvé."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne:{e}"}), 500


# Route pour récupérer tous les groupes
@groupe_controller.route('/', methods=['GET'])
def get_all_groupes() -> tuple[Response, int]:
    try:
        groupes = GroupeService.get_all_groupes()
        if groupes:
            return jsonify(groupes), 200
        return jsonify({"message": "Aucun groupe trouvé."}), 404
    except Exception as e:
        return jsonify({"message": f"Erreur interne lors de la récupération des groupes {e}."}), 500
