from flask import Blueprint, jsonify, request, Response
from services.temps_service import TempsService

temps_controller = Blueprint('temps', __name__, url_prefix='/temps')

@temps_controller.route('/', methods=['POST'])
def add_temps() -> tuple[Response, int]:
    data = request.get_json()
    date_heure_match = data.get('date_heure_match')
    TempsService.add_temps(date_heure_match)
    return jsonify(data), 201

@temps_controller.route('/<int:id_temps>', methods=['DELETE'])
def delete_temps(id_temps) -> tuple[Response, int]:
    success = TempsService.delete_temps(id_temps)
    if success:
        return jsonify({"message": "Le temps a été supprimé avec succès."}), 200
    return jsonify({"message": "La suppression du temps a échoué."}), 400

@temps_controller.route('/<int:id_temps>', methods=['GET'])
def get_temps(id_temps: int) -> tuple[Response, int]:
    temps = TempsService.get_temps(id_temps)
    if temps:
        return jsonify(temps), 200
    return jsonify({"message": "Temps non trouvé."}), 404

@temps_controller.route('/', methods=['GET'])
def get_all_temps() -> tuple[Response, int]:
    temps = TempsService.get_all_temps()
    if temps:
        return jsonify(temps), 200
    return jsonify({"message": "Aucun temps trouvé."}), 404