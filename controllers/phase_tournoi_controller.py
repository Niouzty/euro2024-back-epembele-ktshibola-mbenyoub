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
        return jsonify(data), 201

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
            return jsonify(phase_tournoi), 200
        return jsonify({"error": "Phase du tournoi non trouvée."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération de la phase du tournoi. {e}"}), 500


@phase_tournoi_controller.route('/', methods=['GET'])
def get_all_phases_tournoi() -> tuple[Response, int]:
    try:
        phases_tournoi = PhaseTournoiService.get_all_phases_tournoi()
        if phases_tournoi:
            return jsonify(phases_tournoi), 200
        return jsonify({"error": "Aucune phase du tournoi trouvée."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération des phases du tournoi. {e}"}), 500
