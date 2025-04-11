from flask import Blueprint, jsonify, request, Response
from services.joueur_service import JoueurService

joueur_controller = Blueprint('joueurs', __name__, url_prefix='/joueurs')


# Route pour ajouter un joueur
@joueur_controller.route('/', methods=['POST'])
def add_joueur() -> tuple[Response, int]:
    try:
        data = request.get_json()
        nom = data.get('nom')
        prenom = data.get('prenom')
        date_naissance = data.get('date_naissance')
        id_nationalite = data.get('id_nationalite')
        id_poste = data.get('id_poste')
        num_maillot = data.get('num_maillot')
        id_equipe = data.get('id_equipe')

        if not all([nom, prenom, date_naissance, id_nationalite, id_poste, num_maillot, id_equipe]):
            return jsonify({"error": "Tous les champs sont requis."}), 400

        JoueurService.add_joueur(nom, prenom, date_naissance, id_nationalite, id_poste, num_maillot, id_equipe)
        return jsonify({"result": data}), 201
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de l'ajout du joueur. {e}"}), 500


# Route pour supprimer un joueur
@joueur_controller.route('/<int:id_joueur>', methods=['DELETE'])
def delete_joueur(id_joueur) -> tuple[Response, int]:
    try:
        success = JoueurService.delete_joueur(id_joueur)
        if success:
            return jsonify({"result": "Le joueur a été supprimé avec succès."}), 200
        return jsonify({"error": f"La suppression du joueur a échoué. Le joueur n'existe peut-être pas. "}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne lors de la suppression du joueur. {e}"}), 500


# Route pour récupérer un joueur par ID
@joueur_controller.route('/<int:id_joueur>', methods=['GET'])
def get_joueur(id_joueur: int) -> tuple[Response, int]:
    try:
        joueur = JoueurService.get_joueur(id_joueur)
        if joueur:
            return jsonify({"result": joueur.to_dict()}), 200
        return jsonify({"error": "Joueur non trouvé."}), 404
    except Exception as e:
        return jsonify({"error": "Erreur interne lors de la récupération du joueur."}), 500


# Route pour récupérer tous les joueurs
@joueur_controller.route('/', methods=['GET'])
def get_all_joueurs() -> tuple[Response, int]:
    try:
        offset = int(request.args.get('offset', 0))
        limit = int(request.args.get('limit', 10))

        gs = JoueurService.get_joueurs(offset=offset, limit=limit)
        return jsonify({"result": [g.to_dict() for g in gs]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@joueur_controller.route('/nombres', methods=['GET'])
def get_nombre():
    try:
        total = JoueurService.get_number_row()
        return jsonify({"result": total})
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500

