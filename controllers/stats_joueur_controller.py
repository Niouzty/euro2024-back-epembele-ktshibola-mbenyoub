from flask import Blueprint, jsonify, request, Response
from services.stats_joueur_service import StatsJoueurService

stats_joueur_controller = Blueprint('stats_joueurs', __name__, url_prefix='/stats_joueurs')

@stats_joueur_controller.route('/', methods=['POST'])
def add_stats_joueur() -> tuple[Response, int]:
    data = request.get_json()
    buts_marques = data.get('buts_marques')
    passes_decisives = data.get('passes_decisives')
    cartons_jaunes = data.get('cartons_jaunes')
    cartons_rouges = data.get('cartons_rouges')
    minutes_jouees = data.get('minutes_jouees')
    StatsJoueurService.add_stats_joueur(buts_marques, passes_decisives, cartons_jaunes, cartons_rouges, minutes_jouees)
    return jsonify(data), 201

@stats_joueur_controller.route('/<int:id_stats_joueur>', methods=['DELETE'])
def delete_stats_joueur(id_stats_joueur) -> tuple[Response, int]:
    success = StatsJoueurService.delete_stats_joueur(id_stats_joueur)
    if success:
        return jsonify({"message": "Les statistiques du joueur ont été supprimées avec succès."}), 200
    return jsonify({"message": "La suppression des statistiques du joueur a échoué."}), 400

@stats_joueur_controller.route('/<int:id_stats_joueur>', methods=['GET'])
def get_stats_joueur(id_stats_joueur: int) -> tuple[Response, int]:
    stats_joueur = StatsJoueurService.get_stats_joueur(id_stats_joueur)
    if stats_joueur:
        return jsonify(stats_joueur), 200
    return jsonify({"message": "Statistiques du joueur non trouvées."}), 404

@stats_joueur_controller.route('/', methods=['GET'])
def get_all_stats_joueurs() -> tuple[Response, int]:
    stats_joueurs = StatsJoueurService.get_all_stats_joueurs()
    if stats_joueurs:
        return jsonify(stats_joueurs), 200
    return jsonify({"message": "Aucune statistique de joueur trouvée."}), 404

@stats_joueur_controller.route('/top-buteurs', methods=['GET'])
def get_top_joueur() -> tuple [Response, int]:
    stats_joueurs = StatsJoueurService.get_top_butteurs()
    if stats_joueurs:
        return jsonify(stats_joueurs), 200
    return jsonify({"message": "Aucun joueur trouvé."}), 404