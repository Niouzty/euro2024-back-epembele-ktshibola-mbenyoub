from flask import Flask, jsonify
from controllers.database_controller import database_bp
from controllers.drapeau_controller import drapeau_controller
from controllers.entraineur_controller import entraineur_controller
from controllers.equipe_controller import equipe_controller
from controllers.groupe_controller import groupe_controller
from controllers.joueur_controller import joueur_controller
from controllers.nationalite_controller import nationalite_controller
from controllers.poste_controller import poste_controller
from controllers.rencontre_controller import rencontre_controller
from controllers.resultat_controller import resultat_controller
from controllers.stade_controller import stade_controllers
from controllers.stats_joueur_controller import stats_joueur_controller
from controllers.arbitre_controller import arbitre_bp
from flask_cors import CORS

from controllers.temps_controller import temps_controller
from controllers.ville_controller import ville_controller

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({"message": "Bienvenue sur l'API Euro 2024"}), 200

app.register_blueprint(temps_controller)
app.register_blueprint(ville_controller)
app.register_blueprint(resultat_controller)
app.register_blueprint(entraineur_controller)
app.register_blueprint(drapeau_controller)


app.register_blueprint(poste_controller)
app.register_blueprint(rencontre_controller)
app.register_blueprint(groupe_controller)
app.register_blueprint(nationalite_controller)

app.register_blueprint(database_bp)
app.register_blueprint(equipe_controller)
app.register_blueprint(joueur_controller)
app.register_blueprint(stats_joueur_controller)
app.register_blueprint(arbitre_bp)
app.register_blueprint(stade_controllers)
if __name__ == '__main__':
    app.run(debug=True)  
