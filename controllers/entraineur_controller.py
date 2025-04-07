from flask import Blueprint, jsonify, request, Response
from services.entraineur_service import EntraineurService

entraineur_controller = Blueprint('entraineurs', __name__, url_prefix='/entraineurs')

@entraineur_controller.route('/', methods=['POST'])
def add_entraineur() -> tuple[Response, int]:
    try:
        data = request.get_json()
        nom = data.get('nom')
        prenom = data.get('prenom')
        id_nationalite = data.get('id_nationalite')

        if not data or not nom or not prenom or id_nationalite is None:
            return jsonify({"error": "Données manquantes"}), 400

        if nom.strip() == '' or prenom.strip() == '':
            return jsonify({"error": "Nom ou prénom vide"}), 400

        EntraineurService.add_entraineur(nom, prenom, id_nationalite)
        return jsonify({"message": "Entraîneur ajouté avec succès."}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@entraineur_controller.route('/<int:id_entraineur>', methods=['DELETE'])
def delete_entraineur(id_entraineur) -> tuple[Response, int]:
    try:
        success = EntraineurService.delete_entraineur(id_entraineur)
        if success:
            return jsonify({"message": "L'entraîneur a été supprimé avec succès."}), 200
        return jsonify({"error": "Aucun entraîneur trouvé avec cet ID."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@entraineur_controller.route('/<int:id_entraineur>', methods=['GET'])
def get_entraineur(id_entraineur: int) -> tuple[Response, int]:
    try:
        entraineur = EntraineurService.get_entraineur(id_entraineur)
        if entraineur:
            return jsonify(entraineur), 200
        return jsonify({"error": "Entraîneur non trouvé."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@entraineur_controller.route('/', methods=['GET'])
def get_all_entraineurs() -> tuple[Response, int]:
    try:
        entraineurs = EntraineurService.get_all_entraineurs()
        if entraineurs:
            return jsonify(entraineurs), 200
        return jsonify({"message": "Aucun entraîneur trouvé."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
