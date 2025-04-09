from flask import Blueprint, jsonify, request, Response
from services.nationalite_service import NationaliteService

nationalite_controller = Blueprint('nationalites', __name__, url_prefix='/nationalites')


# Route pour ajouter une nationalité
@nationalite_controller.route('/', methods=['POST'])
def add_nationalite() -> tuple[Response, int]:
    try:
        data = request.get_json()
        nom = data.get('nom')

        if not nom:
            return jsonify({"error": "Le nom de la nationalité est requis."}), 400

        # Ajouter la nationalité en utilisant le service
        NationaliteService.add_nationalite(nom)
        return jsonify({"result": data}), 201

    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de l'ajout de la nationalité. {e}"}), 500


# Route pour supprimer une nationalité
@nationalite_controller.route('/<int:id_nationalite>', methods=['DELETE'])
def delete_nationalite(id_nationalite) -> tuple[Response, int]:
    try:
        success = NationaliteService.delete_nationalite(id_nationalite)
        if success:
            return jsonify({"message": "La nationalité a été supprimée avec succès."}), 200
        return jsonify(
            {"error": "La suppression de la nationalité a échoué. La nationalité n'existe peut-être pas."}), 404
    except Exception as e:
        return jsonify({"message": f"Erreur interne lors de la suppression de la nationalité. {e}"}), 500


# Route pour récupérer une nationalité par ID
@nationalite_controller.route('/<int:id_nationalite>', methods=['GET'])
def get_nationalite(id_nationalite: int) -> tuple[Response, int]:
    try:
        nationalite = NationaliteService.get_nationalite(id_nationalite)
        if nationalite:
            return jsonify({"result": nationalite.to_dict()}), 200
        return jsonify({"error": "Nationalité non trouvée."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération de la nationalité.{e}"}), 500


# Route pour récupérer toutes les nationalités
@nationalite_controller.route('/', methods=['GET'])
def get_all_nationalites() -> tuple[Response, int]:
    try:
        nationalites = NationaliteService.get_all_nationalites()
        if nationalites:
            return jsonify({"result": [nationalite.to_dict() for nationalite in nationalites]}), 200
        return jsonify({"error": "Aucune nationalité trouvée."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération des nationalités. {e}"}), 500
