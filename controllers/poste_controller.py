from flask import Blueprint, jsonify, request, Response
from services.poste_service import PosteService

poste_controller = Blueprint('postes', __name__, url_prefix='/postes')


# Route pour ajouter un poste
@poste_controller.route('/', methods=['POST'])
def add_poste() -> tuple[Response, int]:
    try:
        data = request.get_json()
        nom_poste = data.get('nom_poste')

        if not nom_poste:
            return jsonify({"error": "Le nom du poste est requis."}), 400

        PosteService.add_poste(nom_poste)
        return jsonify(data), 201

    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de l'ajout du poste. {e}"}), 500


# Route pour supprimer un poste
@poste_controller.route('/<int:id_poste>', methods=['DELETE'])
def delete_poste(id_poste: int) -> tuple[Response, int]:
    try:
        success = PosteService.delete_poste(id_poste)
        if success:
            return jsonify({"message": "Le poste a été supprimé avec succès."}), 200
        return jsonify({"error": "La suppression du poste a échoué. Le poste n'existe peut-être pas."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la suppression du poste. {e}"}), 500


# Route pour récupérer un poste par ID
@poste_controller.route('/<int:id_poste>', methods=['GET'])
def get_poste(id_poste: int) -> tuple[Response, int]:
    try:
        poste = PosteService.get_poste(id_poste)
        if poste:
            return jsonify(poste), 200
        return jsonify({"error": "Poste non trouvé."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération du poste. {e}"}), 500


# Route pour récupérer tous les postes
@poste_controller.route('/', methods=['GET'])
def get_all_postes() -> tuple[Response, int]:
    try:
        postes = PosteService.get_all_postes()
        if postes:
            return jsonify(postes), 200
        return jsonify({"error": "Aucun poste trouvé."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération des postes. {e}"}), 500
