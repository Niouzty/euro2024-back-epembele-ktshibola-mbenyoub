from flask import Blueprint, request, jsonify
from services.arbitre_service import ArbitreService

arbitre_bp = Blueprint('arbitre', __name__,'arbitres')

@arbitre_bp.route('/', methods=['POST'])
def add_arbitre():
    data = request.get_json()
    nom = data.get('nom')
    prenom = data.get('prenom')
    id_nationalite = data.get('id_nationalite')

    if not nom or not prenom or not id_nationalite:
        return jsonify({"erreur": "Champs manquants"}), 400

    try:
        ArbitreService.add_arbitre(nom, prenom, id_nationalite)
        return jsonify({"result": data}), 201
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500


@arbitre_bp.route('/<int:id_arbitre>', methods=['DELETE'])
def delete_arbitre(id_arbitre):
    try:
        deleted = ArbitreService.delete_arbitre(id_arbitre)
        if deleted:
            return jsonify({"result": "Arbitre supprimé avec succès."})
        else:
            return jsonify({"erreur": "Arbitre non trouvé."}), 404
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500


@arbitre_bp.route('/<int:id_arbitre>', methods=['GET'])
def get_arbitre(id_arbitre):
    try:
        arbitre = ArbitreService.get_arbitre(id_arbitre)
        if arbitre:
            return jsonify({"result" : arbitre.to_dict()})
        else:
            return jsonify({"erreur": "Arbitre non trouvé."}), 404
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500


@arbitre_bp.route('/', methods=['GET'])
def get_arbitres():
    try:
        arbitres = ArbitreService.get_all_arbitres()
        return jsonify({"result" : [arbitre.to_dict() for arbitre in arbitres]})
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500


@arbitre_bp.route('/resultats', methods=['GET'])
def get_statistiques_arbitres():
    try:
        resultats = ArbitreService.get_all_result()
        return jsonify(resultats)
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500
