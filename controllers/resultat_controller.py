from flask import Blueprint, jsonify, request, Response
from services.resultat_service import ResultatService

resultat_controller = Blueprint('resultats', __name__, url_prefix='/resultats')

@resultat_controller.route('/', methods=['POST'])
def add_resultat() -> tuple[Response, int]:
    data = request.get_json()
    buts_equipe1 = data.get('buts_equipe1_temps_reglementaire')
    buts_equipe2 = data.get('buts_equipe2_temps_reglementaire')
    prolongation = data.get('prolongation')
    tirs_au_but = data.get('tirs_au_but')
    buts_equipe1_prolongation = data.get('buts_equipe1_apres_prolongation')
    buts_equipe2_prolongation = data.get('buts_equipe2_apres_prolongation')
    score_tirs_equipe1 = data.get('score_tirs_au_but_equipe1')
    score_tirs_equipe2 = data.get('score_tirs_au_but_equipe2')
    ResultatService.add_resultat(buts_equipe1, buts_equipe2, prolongation, tirs_au_but, buts_equipe1_prolongation, buts_equipe2_prolongation, score_tirs_equipe1, score_tirs_equipe2)
    return jsonify(data), 201

@resultat_controller.route('/<int:id_resultat>', methods=['DELETE'])
def delete_resultat(id_resultat) -> tuple[Response, int]:
    success = ResultatService.delete_resultat(id_resultat)
    if success:
        return jsonify({"message": "Le résultat a été supprimé avec succès."}), 200
    return jsonify({"message": "La suppression du résultat a échoué."}), 400

@resultat_controller.route('/<int:id_resultat>', methods=['GET'])
def get_resultat(id_resultat: int) -> tuple[Response, int]:
    resultat = ResultatService.get_resultat(id_resultat)
    if resultat:
        return jsonify(resultat), 200
    return jsonify({"message": "Résultat non trouvé."}), 404

@resultat_controller.route('/', methods=['GET'])
def get_all_resultats() -> tuple[Response, int]:
    resultats = ResultatService.get_all_resultats()
    if resultats:
        return jsonify(resultats), 200
    return jsonify({"message": "Aucun résultat trouvé."}), 404


