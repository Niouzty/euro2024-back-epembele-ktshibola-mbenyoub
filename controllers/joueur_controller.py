from flask import Blueprint, jsonify, request, Response
from services.joueur_service import JoueurService

joueur_controller = Blueprint('joueurs', __name__, url_prefix='/joueurs')

@joueur_controller.route('/', methods=['POST'])
def add_joueur() -> tuple[Response, int]:
    data = request.get_json()
    nom = data.get('nom')
    prenom = data.get('prenom')
    date_naissance = data.get('date_naissance')
    id_nationalite = data.get('id_nationalite')
    id_poste = data.get('id_poste')
    num_maillot = data.get('num_maillot')
    id_equipe = data.get('id_equipe')
    JoueurService.add_joueur(nom, prenom, date_naissance, id_nationalite, id_poste, num_maillot, id_equipe)
    return jsonify(data), 201

@joueur_controller.route('/<int:id_joueur>', methods=['DELETE'])
def delete_joueur(id_joueur) -> tuple[Response, int]:
    success = JoueurService.delete_joueur(id_joueur)
    if success:
        return jsonify({"message": "Le joueur a été supprimé avec succès."}), 200
    return jsonify({"message": "La suppression du joueur a échoué."}), 400

@joueur_controller.route('/<int:id_joueur>', methods=['GET'])
def get_joueur(id_joueur: int) -> tuple[Response, int]:
    joueur = JoueurService.get_joueur(id_joueur)
    if joueur:
        return jsonify(joueur), 200
    return jsonify({"message": "Joueur non trouvé."}), 404

@joueur_controller.route('/', methods=['GET'])
def get_all_joueurs() -> tuple[Response, int]:
    joueurs = JoueurService.get_all_joueurs()
    if joueurs:
        return jsonify(joueurs), 200
    return jsonify({"message": "Aucun joueur trouvé."}), 404