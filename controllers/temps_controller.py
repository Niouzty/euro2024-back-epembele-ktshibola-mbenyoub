from flask import Blueprint, jsonify, request, Response
from services.temps_service import TempsService

temps_controller = Blueprint('temps', __name__, url_prefix='/temps')


# ➕ Ajouter une date/heure de match
@temps_controller.route('/', methods=['POST'])
def add_temps() -> tuple[Response, int]:
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Données JSON manquantes ou invalides."}), 400

        date_heure_match = data.get('date_heure_match')
        if not date_heure_match:
            return jsonify({"error": "Champ 'date_heure_match' requis."}), 400

        TempsService.add_temps(date_heure_match)
        return jsonify({"result": data}), 201

    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de l'ajout du temps. {e}"}), 500


# ❌ Supprimer un temps par ID
@temps_controller.route('/<int:id_temps>', methods=['DELETE'])
def delete_temps(id_temps: int) -> tuple[Response, int]:
    try:
        success = TempsService.delete_temps(id_temps)
        if success:
            return jsonify({"result": "Le temps a été supprimé avec succès."}), 200
        return jsonify({"error": "Suppression échouée. Le temps n'existe peut-être pas."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la suppression du temps. {e}"}), 500


# 🔍 Récupérer un temps par ID
@temps_controller.route('/<int:id_temps>', methods=['GET'])
def get_temps(id_temps: int) -> tuple[Response, int]:
    try:
        temps = TempsService.get_temps(id_temps)
        if temps:
            return jsonify({"result": temps.to_dict()}), 200
        return jsonify({"error": "Temps non trouvé."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération du temps. {e}"}), 500


# 📄 Récupérer tous les temps
@temps_controller.route('/', methods=['GET'])
def get_all_temps() -> tuple[Response, int]:
    try:
        temps = TempsService.get_all_temps()
        if temps:
            return jsonify({"result":[ tempsR.to_dict() for tempsR in temps]}), 200
        return jsonify({"error": "Aucun temps trouvé."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération des temps. {e}"}), 500
