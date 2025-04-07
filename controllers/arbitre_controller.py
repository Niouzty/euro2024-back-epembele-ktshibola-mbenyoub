from flask import Blueprint, jsonify, request, Response
from services.arbitre_service import ArbitreService

arbitre_controller = Blueprint('arbitres', __name__, url_prefix='/arbitres')

@arbitre_controller.route('/', methods=['POST'])
def add_arbitre() -> tuple[Response, int]:
    data = request.get_json()
    nom = data.get('nom')
    prenom = data.get('prenom')
    id_nationalite = data.get('id_nationalite')
    ArbitreService.add_arbitre(nom, prenom, id_nationalite)
    return jsonify(data), 201

@arbitre_controller.route('/<int:id_arbitre>', methods=['DELETE'])
def delete_arbitre(id_arbitre) -> tuple[Response, int]:
    success = ArbitreService.delete_arbitre(id_arbitre)
    if success:
        return jsonify({"message": "L'arbitre a été supprimé avec succès."}), 200
    return jsonify({"message": "La suppression de l'arbitre a échoué."}), 400

@arbitre_controller.route('/<int:id_arbitre>', methods=['GET'])
def get_arbitre(id_arbitre: int) -> tuple[Response, int]:
    arbitre = ArbitreService.get_arbitre(id_arbitre)
    if arbitre:
        return jsonify(arbitre), 200
    return jsonify({"message": "Arbitre non trouvé."}), 404

@arbitre_controller.route('/', methods=['GET'])
def get_all_arbitres() -> tuple[Response, int]:
    arbitres = ArbitreService.get_all_arbitres()
    if arbitres:
        print(arbitres)
        return jsonify(arbitres), 200
    return jsonify({"message": "Aucun arbitre trouvé."}), 404

@arbitre_controller.route('/arbitre-result', methods=['GET'])
def get_all_result() -> tuple[Response, int]:
    arbitre = ArbitreService.get_all_result()
    if arbitre:
        return jsonify(arbitre), 
    return jsonify({"messge": "Arbitre nonn trouvé"}), 404