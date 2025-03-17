from flask import Blueprint, jsonify, request, Response
from services.equipe_service import EquipeService

equipe_controller = Blueprint('equipe', __name__, url_prefix='/equipe')

@equipe_controller.route('/', methods=['POST'])
def add_equipe() -> tuple[Response, int]:
    data = request.get_json()
    nom = data.get('Nom')
    groupe = data.get('Groupe')
    entraineur= data.get('Entraineur')
    EquipeService.add_equipe(nom, groupe, entraineur)
    return jsonify(data), 201


@equipe_controller.route('/', methods=['DELETE'])
def delete_equipe(equipe_id):
    success = EquipeService.delete_equipe(equipe_id)

    if success:
        return jsonify({"message": "L'équipe a été supprimée avec succès."}), 200
    return jsonify({"messsge": "La suppression de l'équipe a échoué."}), 400


@equipe_controller.route('/<int: Id_Equipe>', methods=['GET'])
def get_Equipe(equipe_id: int) ->tuple[Response,int]:
    equipe = EquipeService.get_equipe(equipe_id)
    if equipe:
        return jsonify({"message": "Équipe récupérée avec succès."}),200
    return jsonify({"message": "Équipe non trouvée."}), 404


@equipe_controller.route('/equipe', methods=['GET'])
def get_all_equipes_route():
    equipes = EquipeService.get_all_equipes()
    if equipes:
        return jsonify({"message": "Équipes récupérées avec succès.", "data": equipes}), 200
    return jsonify({"message": "Aucune équipe trouvée."}), 404


@equipe_controller.route('/equipe/groupe/<string:groupe>', methods=['GET'])
def get_equipes_by_groupe_route(groupe: str):
    equipes = EquipeService.get_equipes_by_groupe(groupe)
    if equipes:
        return jsonify({"message": f"Équipes du groupe {groupe} récupérées avec succès.","data": equipes}), 200
    return jsonify({"message": f"Aucune équipe trouvée dans le groupe {groupe}."}), 404