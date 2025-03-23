from flask import Blueprint, jsonify, request, Response
from services.rencontre_service import RencontreService

rencontre_controller = Blueprint('matchs', __name__, url_prefix='/matchs')

@rencontre_controller.route('/', methods=['POST'])
def add_rencontre() -> tuple[Response, int]:
    data = request.get_json()
    if not data:
        return jsonify({"message": "Données invalides."}), 400
    
    score_final = data.get('score_Final')
    phase_tournoi = data.get('phase_Tournoi')
    date = data.get('date')
    id_stade = data.get('id_stade')
    id_equipe = data.get('id_equipe')
    id_equipe_equipeb = data.get('id_equipe_equipeb')
    
    success = RencontreService.add_rencontre(score_final, phase_tournoi, date, id_stade, id_equipe, id_equipe_equipeb)
    if success:
        return jsonify({"message": "Rencontre ajoutée avec succès."}), 201
    return jsonify({"message": "Erreur lors de l'ajout de la rencontre."}), 500

@rencontre_controller.route('/<int:id_match>', methods=['DELETE'])
def delete_rencontre(id_match) -> tuple[Response, int]:
    success = RencontreService.delete_rencontre(id_match)
    if success:
        return jsonify({"message": "Rencontre supprimée avec succès."}), 200
    return jsonify({"message": "Erreur lors de la suppression de la rencontre."}), 400

@rencontre_controller.route('/<int:id_match>', methods=['GET'])
def get_rencontre(id_match) -> tuple[Response, int]:
    rencontre = RencontreService.get_rencontre(id_match)
    if rencontre:
        return jsonify(rencontre), 200
    return jsonify({"message": "Rencontre non trouvée."}), 404

@rencontre_controller.route('/', methods=['GET'])
def get_all_rencontres() -> tuple[Response, int]:
    rencontres = RencontreService.get_all_rencontres()
    return jsonify({"message": "Rencontres récupérées avec succès.", "data": rencontres}), 200
