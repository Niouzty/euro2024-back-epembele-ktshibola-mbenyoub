from flask import Blueprint, jsonify, request, Response
from services.drapeau_service import DrapeauService

drapeau_controller = Blueprint('drapeaux', __name__, url_prefix='/drapeaux')


@drapeau_controller.route('/', methods=['POST'])
def add_drapeau() -> tuple[Response, int]:
    try:
        data = request.get_json()
        id_equipe = data.get('id_equipe')
        chemin_image = data.get('chemin_image')

        if not data or id_equipe is None or not chemin_image:
            return jsonify({"error": "Données manquantes"}), 400

        if str(chemin_image).strip() == "":
            return jsonify({"error": "Chemin de l'image vide"}), 400

        DrapeauService.add_drapeau(id_equipe, chemin_image)
        return jsonify({"result": data}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@drapeau_controller.route('/<int:id_drapeau>', methods=['DELETE'])
def delete_drapeau(id_drapeau: int) -> tuple[Response, int]:
    try:
        success = DrapeauService.delete_drapeau(id_drapeau)
        if success:
            return jsonify({"result": "Le drapeau a été supprimé avec succès."}), 200
        return jsonify({"error": "Aucun drapeau trouvé avec cet ID."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@drapeau_controller.route('/<int:id_drapeau>', methods=['GET'])
def get_drapeau(id_drapeau: int) -> tuple[Response, int]:
    try:
        drapeau = DrapeauService.get_drapeau(id_drapeau)
        if drapeau:
            return jsonify({"result": drapeau.to_dict()}), 200
        return jsonify({"error": "Drapeau non trouvé."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@drapeau_controller.route('/', methods=['GET'])
def get_all_drapeaux() -> tuple[Response, int]:
    try:
        offset = int(request.args.get('offset', 0))
        limit = int(request.args.get('limit', 10))

        drapeaux = DrapeauService.get_all_drapeaux(offset=offset, limit=limit)
        return jsonify({"result": [drapeau.to_dict() for drapeau in drapeaux]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@drapeau_controller.route('/nombres', methods=['GET'])
def get_nombre_arbitres():
    try:
        total = DrapeauService.get_number_row()
        return jsonify({"result": total})
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500

@drapeau_controller.route('/nombres', methods=['GET'])
def get_nombre_drapeaux() -> tuple[Response, int]:
    try:
        total = DrapeauService.get_number_row()
        return jsonify({"result": total}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
