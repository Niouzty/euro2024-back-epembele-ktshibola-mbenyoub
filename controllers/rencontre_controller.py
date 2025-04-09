from flask import Blueprint, jsonify, request, Response
from services.rencontre_service import RencontreService

rencontre_controller = Blueprint('matchs', __name__, url_prefix='/matchs')


# Route pour ajouter une rencontre
@rencontre_controller.route('/', methods=['POST'])
def add_rencontre() -> tuple[Response, int]:
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Données JSON manquantes ou invalides."}), 400

        score_final = data.get('score_Final')
        phase_tournoi = data.get('phase_Tournoi')
        date = data.get('date')
        id_stade = data.get('id_stade')
        id_equipe = data.get('id_equipe')
        id_equipe_equipeb = data.get('id_equipe_equipeb')

        champs_manquants = []
        if score_final is None: champs_manquants.append("score_Final")
        if phase_tournoi is None: champs_manquants.append("phase_Tournoi")
        if date is None: champs_manquants.append("date")
        if id_stade is None: champs_manquants.append("id_stade")
        if id_equipe is None: champs_manquants.append("id_equipe")
        if id_equipe_equipeb is None: champs_manquants.append("id_equipe_equipeb")

        if champs_manquants:
            return jsonify({"error": f"Champs requis manquants : {', '.join(champs_manquants)}"}), 400

        success = RencontreService.add_rencontre(
            score_final, phase_tournoi, date, id_stade, id_equipe, id_equipe_equipeb
        )
        if success:
            return jsonify({"result": data}), 201

        return jsonify({"error": "Erreur lors de l'ajout de la rencontre."}), 500

    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de l'ajout de la rencontre. {e}"}), 500


# Route pour supprimer une rencontre
@rencontre_controller.route('/<int:id_match>', methods=['DELETE'])
def delete_rencontre(id_match: int) -> tuple[Response, int]:
    try:
        success = RencontreService.delete_rencontre(id_match)
        if success:
            return jsonify({"result": "Rencontre supprimée avec succès."}), 200
        return jsonify({"error": "Suppression échouée. La rencontre n'existe peut-être pas."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la suppression de la rencontre. {e}"}), 500


# Route pour récupérer une rencontre par ID
@rencontre_controller.route('/<int:id_match>', methods=['GET'])
def get_rencontre(id_match: int) -> tuple[Response, int]:
    try:
        rencontre = RencontreService.get_rencontre(id_match)
        if rencontre:
            return jsonify({"result": rencontre.to_dict()}), 200
        return jsonify({"error": "Rencontre non trouvée."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération de la rencontre. {e}"}), 500


# Route pour récupérer toutes les rencontres
@rencontre_controller.route('/', methods=['GET'])
def get_all_rencontres() -> tuple[Response, int]:
    try:
        rencontres = RencontreService.get_all_rencontres()
        if rencontres:
            return jsonify({"result": [rencontre.to_dict() for rencontre in rencontres]}), 200
        return jsonify({"error": "Aucune rencontre trouvée."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération des rencontres. {e}"}), 500
