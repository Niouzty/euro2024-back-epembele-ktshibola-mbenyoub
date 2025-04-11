from typing import Tuple

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
        return jsonify({"result": data}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@entraineur_controller.route('/<int:id_entraineur>', methods=['DELETE'])
def delete_entraineur(id_entraineur) -> tuple[Response, int]:
    try:
        success = EntraineurService.delete_entraineur(id_entraineur)
        if success:
            return jsonify({"result": "L'entraîneur a été supprimé avec succès."}), 200
        return jsonify({"error": "Aucun entraîneur trouvé avec cet ID."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@entraineur_controller.route('/<int:id_entraineur>', methods=['GET'])
def get_entraineur(id_entraineur: int) -> tuple[Response, int]:
    try:
        entraineur = EntraineurService.get_entraineur(id_entraineur)
        if entraineur:
            return jsonify({"result": entraineur.to_dict()}), 200
        return jsonify({"error": "Entraîneur non trouvé."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@entraineur_controller.route('/', methods=['GET'])
def get_all_entraineurs() -> tuple[Response, int]:
    try:
        offset = int(request.args.get('offset', 0))
        limit = int(request.args.get('limit', 10))

        es = EntraineurService.get_all_entraineurs(offset, limit)
        return jsonify({"result": [e.to_dict() for e in es]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@entraineur_controller.route('/nombres', methods=['GET'])
def get_nombre_arbitres():
    try:
        total = EntraineurService.get_number_row()
        return jsonify({"result": total})
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500




@entraineur_controller.route('/nombres', methods=['GET'])
def get_nombre_entraineurs() -> tuple[Response, int]:
    try:
        total = EntraineurService.get_number_row()
        return jsonify({"result": total}),200
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500
