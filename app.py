from flask import Flask, jsonify
from controllers.database_controller import database_controller
from controllers.equipe_controller import equipe_controller 
from controllers.joueur_controller import joueur_controller
from controllers.stats_joueur_controller import stats_joueur_controller
from controllers.arbitre_controller import arbitre_controller
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({"message": "Bienvenue sur l'API Euro 2024"}), 200

app.register_blueprint(database_controller)
app.register_blueprint(equipe_controller)
app.register_blueprint(joueur_controller)
app.register_blueprint(stats_joueur_controller)
app.register_blueprint(arbitre_controller)


if __name__ == '__main__':
    app.run(debug=True)  
