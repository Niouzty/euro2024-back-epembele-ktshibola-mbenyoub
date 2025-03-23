from flask import Blueprint, jsonify, request, Response
from services.entraineur_service import EntraineurService

entraineur_controller = Blueprint('entraineurs', __name__, url_prefix='/entraineurs')

@entraineur_controller.route('/', methods=['POST'])
def add_entraineur() -> tuple[Response, int]:
    data = request.get_json()
    nom = data.get('nom')
    prenom = data.get('prenom')
    id_nationalite = data.get('id_nationalite')
    EntraineurService.add_entraineur(nom, prenom, id_nationalite)
    return jsonify(data), 201

@entraineur_controller.route('/<int:id_entraineur>', methods=['DELETE'])
def delete_entraineur(id_entraineur) -> tuple[Response, int]:
    success = EntraineurService.delete_entraineur(id_entraineur)
    if success:
        return jsonify({"message": "L'entraîneur a été supprimé avec succès."}), 200
    return jsonify({"message": "La suppression de l'entraîneur a échoué."}), 400

@entraineur_controller.route('/<int:id_entraineur>', methods=['GET'])
def get_entraineur(id_entraineur: int) -> tuple[Response, int]:
    entraineur = EntraineurService.get_entraineur(id_entraineur)
    if entraineur:
        return jsonify(entraineur), 200
    return jsonify({"message": "Entraîneur non trouvé."}), 404

@entraineur_controller.route('/', methods=['GET'])
def get_all_entraineurs() -> tuple[Response, int]:
    entraineurs = EntraineurService.get_all_entraineurs()
    if entraineurs:
        return jsonify(entraineurs), 200
    return jsonify({"message": "Aucun entraîneur trouvé."}), 404