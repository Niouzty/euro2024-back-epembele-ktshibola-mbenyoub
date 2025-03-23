from flask import Blueprint, jsonify, request, Response
from services.equipe_service import EquipeService

equipe_controller = Blueprint('equipes', __name__, url_prefix='/equipes')

@equipe_controller.route('/', methods=['POST'])
def add_equipe() -> tuple[Response, int]:
    data = request.get_json()
    nom = data.get('nom')
    groupe = data.get('groupe')
    entraineur= data.get('entraineur')
    EquipeService.add_equipe(nom, groupe, entraineur)
    return jsonify(data), 201


@equipe_controller.route('/<int: id_equipe>', methods=['DELETE'])
def delete_equipe(id_equipe) -> tuple[Response, int]:
    success = EquipeService.delete_equipe(id_equipe)

    if success:
        return jsonify({"message": "L'équipe a été supprimée avec succès."}), 200
    return jsonify({"messsage": "La suppression de l'équipe a échoué."}), 400


@equipe_controller.route('/<int: id_equipe>', methods=['GET'])
def get_equipe(id_equipe: int) -> tuple[Response,int]:
    equipe = EquipeService.get_equipe(id_equipe)
    if equipe:
        return jsonify({"message": "Équipe récupérée avec succès."}),200
    return jsonify({"message": "Équipe non trouvée."}), 404


@equipe_controller.route('/', methods=['GET'])
def get_all_equipes_route():
    equipes = EquipeService.get_all_equipes()
    if equipes:
        return jsonify({"message": "Équipes récupérées avec succès.", "data": equipes}), 200
    return jsonify({"message": "Aucune équipe trouvée."}), 404
