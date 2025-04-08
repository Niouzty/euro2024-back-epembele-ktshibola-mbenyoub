from flask import Blueprint, jsonify, request, Response
from services.resultat_service import ResultatService

resultat_controller = Blueprint('resultats', __name__, url_prefix='/resultats')


# 🔧 Fonction utilitaire pour vérifier les champs requis
def verifier_champs(data: dict, champs_requis: list[str]) -> list[str]:
    return [champ for champ in champs_requis if data.get(champ) is None]


# ➕ Route pour ajouter un résultat
@resultat_controller.route('/', methods=['POST'])
def add_resultat() -> tuple[Response, int]:
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Données JSON manquantes ou invalides."}), 400

        champs_requis = [
            'buts_equipe1_temps_reglementaire',
            'buts_equipe2_temps_reglementaire',
            'prolongation',
            'tirs_au_but',
            'buts_equipe1_apres_prolongation',
            'buts_equipe2_apres_prolongation',
            'score_tirs_au_but_equipe1',
            'score_tirs_au_but_equipe2'
        ]

        champs_manquants = verifier_champs(data, champs_requis)
        if champs_manquants:
            return jsonify({"error": f"Champs requis manquants : {', '.join(champs_manquants)}"}), 400

        ResultatService.add_resultat(
            data['buts_equipe1_temps_reglementaire'],
            data['buts_equipe2_temps_reglementaire'],
            data['prolongation'],
            data['tirs_au_but'],
            data['buts_equipe1_apres_prolongation'],
            data['buts_equipe2_apres_prolongation'],
            data['score_tirs_au_but_equipe1'],
            data['score_tirs_au_but_equipe2']
        )
        return jsonify({"message": "Résultat ajouté avec succès."}), 201

    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de l'ajout du résultat. {e}"}), 500


# ❌ Route pour supprimer un résultat
@resultat_controller.route('/<int:id_resultat>', methods=['DELETE'])
def delete_resultat(id_resultat: int) -> tuple[Response, int]:
    try:
        success = ResultatService.delete_resultat(id_resultat)
        if success:
            return jsonify({"message": "Le résultat a été supprimé avec succès."}), 200
        return jsonify({"error": "Suppression échouée. Le résultat n'existe peut-être pas."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la suppression du résultat. {e}"}), 500


# 🔍 Route pour récupérer un résultat par ID
@resultat_controller.route('/<int:id_resultat>', methods=['GET'])
def get_resultat(id_resultat: int) -> tuple[Response, int]:
    try:
        resultat = ResultatService.get_resultat(id_resultat)
        if resultat:
            return jsonify(resultat), 200
        return jsonify({"error": "Résultat non trouvé."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération du résultat. {e}"}), 500


# 📄 Route pour récupérer tous les résultats
@resultat_controller.route('/', methods=['GET'])
def get_all_resultats() -> tuple[Response, int]:
    try:
        resultats = ResultatService.get_all_resultats()
        if resultats:
            return jsonify(resultats), 200
        return jsonify({"error": "Aucun résultat trouvé."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération des résultats. {e}"}), 500
