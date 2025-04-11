from flask import Blueprint, jsonify, request, Response
from services.equipe_service import EquipeService

equipe_controller = Blueprint('equipes', __name__, url_prefix='/equipes')


@equipe_controller.route('/', methods=['POST'])
def add_equipe() -> tuple[Response, int]:
    try:
        data = request.get_json()
        nom = data.get('nom')
        groupe = data.get('groupe')
        entraineur = data.get('entraineur')

        if not nom or not groupe or not entraineur:
            return jsonify({"result": "Données manquantes"}), 400

        EquipeService.add_equipe(nom, groupe, entraineur)
        return jsonify({"result": data}), 201
    except Exception as e:
        return jsonify({"error": f"Erreur serveur: {str(e)}"}), 500


@equipe_controller.route('/<int:id_equipe>', methods=['DELETE'])
def delete_equipe(id_equipe) -> tuple[Response, int]:
    try:
        success = EquipeService.delete_equipe(id_equipe)
        if success:
            return jsonify({"result": "L'équipe a été supprimée avec succès."}), 200
        return jsonify({"result": "La suppression de l'équipe a échoué."}), 400
    except Exception as e:
        return jsonify({"error": f"Erreur serveur: {str(e)}"}), 500


@equipe_controller.route('/<int:id_equipe>', methods=['GET'])
def get_equipe(id_equipe: int) -> tuple[Response, int]:
    try:
        equipe = EquipeService.get_equipe(id_equipe)
        if equipe:
            return jsonify({"result": equipe.to_dict()}), 200
        return jsonify({"result": "Équipe non trouvée."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur serveur: {str(e)}"}), 500


@equipe_controller.route('/', methods=['GET'])
def get_all_equipes_route() -> tuple[Response, int]:
    try:
        offset = int(request.args.get('offset', 0))
        limit = int(request.args.get('limit', 10))

        equipes = EquipeService.get_equipes(offset=offset, limit=limit)
        return jsonify({"result": [e.to_dict() for e in equipes]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500




@equipe_controller.route('/nombres', methods=['GET'])
def get_nombre():
    try:
        total = EquipeService.get_number_row()
        return jsonify({"result": total})
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500




@equipe_controller.route('/compare', methods=['POST'])
def compare_teams() -> tuple[Response, int]:
    try:
        data = request.get_json()
        equipe1_id = data.get('equipe1_id')
        equipe2_id = data.get('equipe2_id')

        if not equipe1_id or not equipe2_id:
            return jsonify({"message": "Les IDs des deux équipes sont requis."}), 400

        stats_equipe1 = EquipeService.get_all_result_by_equipe(equipe1_id)
        stats_equipe2 = EquipeService.get_all_result_by_equipe(equipe2_id)

        if not stats_equipe1 or not stats_equipe2:
            return jsonify({"message": "Données introuvables pour une ou plusieurs équipes."}), 404

        # Extraction des données
        e1 = stats_equipe1[0] if stats_equipe1 else {
            'nom': f'Équipe {equipe1_id}',
            'nombre_de_matchs': 0,
            'buts_temps_reglementaire': 0,
            'buts_apres_prolongation': 0,
            'buts_tirs_au_but': 0
        }

        e2 = stats_equipe2[0] if stats_equipe2 else {
            'nom': f'Équipe {equipe2_id}',
            'nombre_de_matchs': 0,
            'buts_temps_reglementaire': 0,
            'buts_apres_prolongation': 0,
            'buts_tirs_au_but': 0
        }

        # Construction de la réponse
        response = {
            "equipe1": {
                "nom": e1['nom'],
                "nombre_de_matchs": e1['nombre_de_matchs'],
                "buts_temps_reglementaire": e1['buts_temps_reglementaire'],
                "buts_apres_prolongation": e1['buts_apres_prolongation'],
                "buts_tirs_au_but": e1['buts_tirs_au_but']
            },
            "equipe2": {
                "nom": e2['nom'],
                "nombre_de_matchs": e2['nombre_de_matchs'],
                "buts_temps_reglementaire": e2['buts_temps_reglementaire'],
                "buts_apres_prolongation": e2['buts_apres_prolongation'],
                "buts_tirs_au_but": e2['buts_tirs_au_but']
            },
            "comparaison": {
                "difference_buts_reglementaire": e1['buts_temps_reglementaire'] - e2['buts_temps_reglementaire'],
                "difference_buts_prolongation": e1['buts_apres_prolongation'] - e2['buts_apres_prolongation'],
                "difference_tirs_au_but": e1['buts_tirs_au_but'] - e2['buts_tirs_au_but'],
                "difference_matchs_joues": e1['nombre_de_matchs'] - e2['nombre_de_matchs']
            }
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": f"Erreur serveur: {str(e)}"}), 500
