from flask import Blueprint, jsonify, request, Response
from services.ville_service import VilleService

ville_controller = Blueprint('villes', __name__, url_prefix='/villes')


# ➕ Ajouter une ville
@ville_controller.route('/', methods=['POST'])
def add_ville() -> tuple[Response, int]:
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Données JSON manquantes ou invalides."}), 400

        nom = data.get('nom')
        if not nom:
            return jsonify({"error": "Le champ 'nom' est requis."}), 400

        VilleService.add_ville(nom)
        return jsonify({"result": data}), 201

    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de l'ajout de la ville. {e}"}), 500


# ❌ Supprimer une ville par ID
@ville_controller.route('/<int:id_ville>', methods=['DELETE'])
def delete_ville(id_ville: int) -> tuple[Response, int]:
    try:
        success = VilleService.delete_ville(id_ville)
        if success:
            return jsonify({"result": "La ville a été supprimée avec succès."}), 200
        return jsonify({"error": "Suppression échouée. La ville n'existe peut-être pas."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la suppression de la ville. {e}"}), 500


# 🔍 Obtenir une ville par son ID
@ville_controller.route('/<int:id_ville>', methods=['GET'])
def get_ville(id_ville: int) -> tuple[Response, int]:
    try:
        ville = VilleService.get_ville(id_ville)
        if ville:
            return jsonify({"result": ville.to_dict()}), 200
        return jsonify({"error": "Ville non trouvée."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération de la ville. {e}"}), 500


# 📄 Obtenir la liste de toutes les villes
@ville_controller.route('/', methods=['GET'])
def get_all_villes() -> tuple[Response, int]:
    try:
        offset = int(request.args.get('offset', 0))
        limit = int(request.args.get('limit', 10))

        ns = VilleService.get_villes(offset=offset, limit=limit)
        return jsonify({"result": [n.to_dict() for n in ns]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@ville_controller.route('/nombres', methods=['GET'])
def get_nombre():
    try:
        total = VilleService.get_number_row()
        return jsonify({"result": total})
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500
