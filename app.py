from flask import Flask
from flask_cors import CORS

from Controllers.controllers_stades import stade_controllers

app = Flask(__name__)
app.register_blueprint(stade_controllers)

CORS(app, resources={
    r"/*": {
        "origins": "*",  # Autoriser toutes les origines
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Méthodes autorisées
        "allow_headers": ["Content-Type", "Authorization"]  # En-têtes autorisés
    }
})
if __name__ == '__main__':
    app.run()
