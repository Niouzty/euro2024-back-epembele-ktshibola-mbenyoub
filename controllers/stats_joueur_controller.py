from flask import Blueprint, jsonify, request, Response
from services.stats_joueur_service import StatsJoueurService

stats_joueur_controller = Blueprint('stats_joueurs', __name__, url_prefix='/stats_joueurs')


# 🔧 Vérifie les champs manquants dans les données
def verifier_champs(data: dict, champs_requis: list[str]) -> list[str]:
    return [champ for champ in champs_requis if data.get(champ) is None]


# ➕ Ajouter des statistiques pour un joueur
@stats_joueur_controller.route('/', methods=['POST'])
def add_stats_joueur() -> tuple[Response, int]:
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Données JSON manquantes ou invalides."}), 400

        champs_requis = [
            'buts_marques',
            'passes_decisives',
            'cartons_jaunes',
            'cartons_rouges',
            'minutes_jouees'
        ]
        champs_manquants = verifier_champs(data, champs_requis)
        if champs_manquants:
            return jsonify({"error": f"Champs requis manquants : {', '.join(champs_manquants)}"}), 400

        StatsJoueurService.add_stats_joueur(
            data['buts_marques'],
            data['passes_decisives'],
            data['cartons_jaunes'],
            data['cartons_rouges'],
            data['minutes_jouees']
        )
        return jsonify({"result": data}), 201

    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de l'ajout des statistiques. {e}"}), 500


# ❌ Supprimer les statistiques d'un joueur
@stats_joueur_controller.route('/<int:id_stats_joueur>', methods=['DELETE'])
def delete_stats_joueur(id_stats_joueur: int) -> tuple[Response, int]:
    try:
        success = StatsJoueurService.delete_stats_joueur(id_stats_joueur)
        if success:
            return jsonify({"result": "Les statistiques du joueur ont été supprimées avec succès."}), 200
        return jsonify({"error": "Suppression échouée. Les statistiques n'existent peut-être pas."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la suppression des statistiques. {e}"}), 500


# 🔍 Récupérer les statistiques d’un joueur par ID
@stats_joueur_controller.route('/<int:id_stats_joueur>', methods=['GET'])
def get_stats_joueur(id_stats_joueur: int) -> tuple[Response, int]:
    try:
        stats_joueur = StatsJoueurService.get_stats_joueur(id_stats_joueur)
        if stats_joueur:
            return jsonify({"result": stats_joueur.to_dict()}), 200
        return jsonify({"error": "Statistiques du joueur non trouvées."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération des statistiques. {e}"}), 500


# 📄 Récupérer toutes les statistiques des joueurs
@stats_joueur_controller.route('/', methods=['GET'])
def get_all_stats_joueurs() -> tuple[Response, int]:
    try:
        stats_joueurs = StatsJoueurService.get_all_stats_joueurs()
        if stats_joueurs:
            return jsonify({"result": [stats_joueur.to_dict() for  stats_joueur in stats_joueurs]}), 200
        return jsonify({"error": "Aucune statistique de joueur trouvée."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération des statistiques. {e}"}), 500


# ⭐ Récupérer les meilleurs buteurs
@stats_joueur_controller.route('/top-buteurs', methods=['GET'])
def get_top_joueur() -> tuple[Response, int]:
    try:
        stats_joueurs = StatsJoueurService.get_top_butteurs()
        print(stats_joueurs)
        if stats_joueurs:
            return jsonify(stats_joueurs), 200
        return jsonify({"error": "Aucun joueur trouvé."}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la récupération des meilleurs buteurs. {e}"}), 500
