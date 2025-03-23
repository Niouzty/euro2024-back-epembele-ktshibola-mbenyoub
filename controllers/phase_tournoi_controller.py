from flask import Blueprint, jsonify, request, Response
from services.phase_tournoi_service import PhaseTournoiService

phase_tournoi_controller = Blueprint('phases_tournoi', __name__, url_prefix='/phases_tournoi')

@phase_tournoi_controller.route('/', methods=['POST'])
def add_phase_tournoi() -> tuple[Response, int]:
    data = request.get_json()
    nom = data.get('nom')
    PhaseTournoiService.add_phase_tournoi(nom)
    return jsonify(data), 201

@phase_tournoi_controller.route('/<int:id_phase>', methods=['DELETE'])
def delete_phase_tournoi(id_phase) -> tuple[Response, int]:
    success = PhaseTournoiService.delete_phase_tournoi(id_phase)
    if success:
        return jsonify({"message": "La phase du tournoi a été supprimée avec succès."}), 200
    return jsonify({"message": "La suppression de la phase du tournoi a échoué."}), 400

@phase_tournoi_controller.route('/<int:id_phase>', methods=['GET'])
def get_phase_tournoi(id_phase: int) -> tuple[Response, int]:
    phase_tournoi = PhaseTournoiService.get_phase_tournoi(id_phase)
    if phase_tournoi:
        return jsonify(phase_tournoi), 200
    return jsonify({"message": "Phase du tournoi non trouvée."}), 404

@phase_tournoi_controller.route('/', methods=['GET'])
def get_all_phases_tournoi() -> tuple[Response, int]:
    phases_tournoi = PhaseTournoiService.get_all_phases_tournoi()
    if phases_tournoi:
        return jsonify(phases_tournoi), 200
    return jsonify({"message": "Aucune phase du tournoi trouvée."}), 404