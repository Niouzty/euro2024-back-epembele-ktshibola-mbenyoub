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
        offset = int(request.args.get('offset', 0))
        limit = int(request.args.get('limit', 10))

        ns = NationaliteService.get_nationalites(offset=offset, limit=limit)
        return jsonify({"result": [n.to_dict() for n in ns]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@nationalite_controller.route('/nombres', methods=['GET'])
def get_nombre():
    try:
        total = NationaliteService.get_number_row()
        return jsonify({"result": total})
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500
