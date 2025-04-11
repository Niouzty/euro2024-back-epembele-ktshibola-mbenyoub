from flask import Blueprint, jsonify, request, Response
from services.phase_tournoi_service import PhaseTournoiService

phase_tournoi_controller = Blueprint('phases_tournoi', __name__, url_prefix='/phases_tournoi')


@phase_tournoi_controller.route('/', methods=['POST'])
def add_phase_tournoi() -> tuple[Response, int]:
    try:
        data = request.get_json()
        nom = data.get('nom')

        if not nom:
            return jsonify({"error": "Le nom de la phase du tournoi est requis."}), 400

        PhaseTournoiService.add_phase_tournoi(nom)
        return jsonify({"result": data}), 201

    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de l'ajout de la phase du tournoi. {e}"}), 500


@phase_tournoi_controller.route('/<int:id_phase>', methods=['DELETE'])
def delete_phase_tournoi(id_phase: int) -> tuple[Response, int]:
    try:
        success = PhaseTournoiService.delete_phase_tournoi(id_phase)
        if success:
            return jsonify({"message": "La phase du tournoi a été supprimée avec succès."}), 200
        return jsonify(
            {"error": "La suppression de la phase du tournoi a échoué. La phase n'existe peut-être pas."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la suppression de la phase du tournoi. {e}"}), 500


@phase_tournoi_controller.route('/<int:id_phase>', methods=['GET'])
def get_phase_tournoi(id_phase: int) -> tuple[Response, int]:
    try:
        phase_tournoi = PhaseTournoiService.get_phase_tournoi(id_phase)
        if phase_tournoi:
            return jsonify({"result": phase_tournoi.to_dict()}), 200
        return jsonify({"error": "Phase du tournoi non trouvée."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération de la phase du tournoi. {e}"}), 500


@phase_tournoi_controller.route('/', methods=['GET'])
def get_all_phases_tournoi() -> tuple[Response, int]:
    try:
        offset = int(request.args.get('offset', 0))
        limit = int(request.args.get('limit', 10))

        ns = PhaseTournoiService.get_phase_tournois(offset=offset, limit=limit)
        return jsonify({"result": [n.to_dict() for n in ns]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@phase_tournoi_controller.route('/nombres', methods=['GET'])
def get_nombre():
    try:
        total = PhaseTournoiService.get_number_row()
        return jsonify({"result": total})
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500
