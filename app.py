from flask import Flask
from flask_cors import CORS

from Controllers.bdd_controllers import bdd_controllers
from Controllers.controllers_stades import stade_controllers

app = Flask(__name__)
app.register_blueprint(stade_controllers)
app.register_blueprint(bdd_controllers)

CORS(app, resources={
    r"/*": {
        "origins": "*",  # Autoriser toutes les origines
        "methods": ["GET", "POST", "PUT", "DELETE", "PATCH"],  # Méthodes autorisées
        "allow_headers": ["Content-Type", "Authorization"]  # En-têtes autorisés
    }
})
if __name__ == '__main__':
    app.run()
