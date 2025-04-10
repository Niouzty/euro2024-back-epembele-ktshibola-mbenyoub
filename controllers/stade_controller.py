from flask import Blueprint, request, jsonify

from services.stade_service import StadeService

stade_controllers = Blueprint('stade_controllers', __name__, url_prefix='/stades')


@stade_controllers.route('/', methods=['GET'])
def get_stades():
    try:
        page = request.args.get('offset', default=1, type=int)
        taille_page = request.args.get('limit', default=10, type=int)
        offset = (page - 1) * taille_page

        stades = StadeService.get_stades(offset, taille_page)
        return jsonify({"result" : [stade.to_dict() for stade in stades]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@stade_controllers.route('/<int:stade_id>', methods=['GET'])
def get_stade(stade_id):
    try:
        stade = StadeService.get_stade(stade_id)
        if stade:
            return jsonify({"result" : stade.to_dict()}), 200
        return jsonify({"error": "Stade non trouvé"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500





@stade_controllers.route('/<int:stade_id>', methods=['DELETE'])
def supprimer_stade(stade_id):
    try:
        if not StadeService.stade_exist(stade_id):
            return jsonify({"error": "Stade non trouvé"}), 404

        StadeService.delete_stade(stade_id)
        return jsonify({"result": "Stade supprimé avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e) + " hjhh"}), 500


@stade_controllers.route('/nombres', methods=['GET'])
def get_nombres_stades():
    try:
        taille = StadeService.get_number_row()
        return jsonify({"result": taille}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@stade_controllers.route('/visitors/length', methods=['GET'])
def get_visitors_stades_length():
    try:
        stade_taille = StadeService.get_stade_visitor()
        return jsonify({"result": stade_taille}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@stade_controllers.route('/<int:stade_id>', methods=['PATCH'])
def update_stade(stade_id):
    try:
        data = request.get_json() or {}
        column, value = data.get("column"), data.get("value")

        if not column or value is None:
            return jsonify({"error": "Champs 'column' et 'value' requis"}), 400

        valid_columns = {"nom", "ville", "capacite"}
        if column not in valid_columns:
            return jsonify({"error": f"Colonne '{column}' non autorisée"}), 400

        success = StadeService.update_stade(stade_id, column, value)
        if not success:
            return jsonify({"error": "Erreur lors de la mise à jour du stade"}), 500

        return jsonify({"result": "Stade mis à jour avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500





@stade_controllers.route('/batch', methods=['POST'])
def insert():
    try:
        data = request.get_json() or {}


        if not isinstance(data, list) or not data:
            return jsonify({"error": "Le champ 'stades' doit être une liste non vide"}), 400

        non_inserees = []
        success_count = 0

        for row in data:
            print(row)
            print(row.get("nom"))
            # On vérifie que chaque élément est bien un dictionnaire
            if not isinstance(row, dict):
                non_inserees.append({"error": "Chaque élément doit être un objet (dictionnaire)", "row": row})
                continue

            # Vérification des champs obligatoires
            if not all(key in row and row[key] is not None for key in ("nom", "id_ville", "capacite")):
                row["error"] = "Champs obligatoires manquants : nom, id_ville, capacite"
                non_inserees.append(row)
                continue

            try:
                if row.get('id_stade') is not None:
                    StadeService.add_stade(row['nom'], int(row['id_ville']), int(row['capacite']), int(row['id_stade']))
                else:
                    StadeService.add_stade(row['nom'], int(row['id_ville']), int(row['capacite']))

                success_count += 1

            except Exception as e:
                row["error"] = str(e)
                non_inserees.append(row)

        total = len(data)

        if success_count == total:
            return jsonify({"result": f"{success_count} stades insérés"}), 201
        elif success_count > 0:
            return jsonify({
                "result": f"{success_count} stades insérés, {len(non_inserees)} échecs",
                "non_inserees": non_inserees
            }), 207
        else:
            return jsonify({
                "error": f"Aucune insertion réussie sur {total} enregistrements",
                "non_inserees": non_inserees
            }), 400

    except Exception as e:
        return jsonify({"error": f"Erreur serveur : {str(e)}"}), 500

