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
        return jsonify({"result": data}), 201
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de l'ajout du groupe. {e}"}), 500


# Route pour supprimer un groupe
@groupe_controller.route('/<int:id_groupe>', methods=['DELETE'])
def delete_groupe(id_groupe) -> tuple[Response, int]:
    try:
        success = GroupeService.delete_groupe(id_groupe)
        if success:
            return jsonify({"result": "Le groupe a été supprimé avec succès."}), 200
        return jsonify({"error": f"La suppression du groupe a échoué. Le groupe n'existe peut-être pas."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la suppression du groupe. {e}"}), 500


# Route pour récupérer un groupe par ID
@groupe_controller.route('/<int:id_groupe>', methods=['GET'])
def get_groupe(id_groupe: int) -> tuple[Response, int]:
    try:
        groupe = GroupeService.get_groupe(id_groupe)
        if groupe:
            return jsonify({"result": groupe.to_dict()}), 200
        return jsonify({"error": "Groupe non trouvé."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne:{e}"}), 500


# Route pour récupérer tous les groupes
@groupe_controller.route('/', methods=['GET'])
def get_all_groupes() -> tuple[Response, int]:
    try:
        offset = int(request.args.get('offset', 0))
        limit = int(request.args.get('limit', 10))

        gs = GroupeService.get_groupes(offset=offset, limit=limit)
        return jsonify({"result": [g.to_dict() for g in gs]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@groupe_controller.route('/nombres', methods=['GET'])
def get_nombre():
    try:
        total = GroupeService.get_number_row()
        return jsonify({"result": total})
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500

