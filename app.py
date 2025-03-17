from flask import Flask, jsonify, request, Blueprint

from controllers.equipe_controller import equipe_controller
from controllers.rencontre_controller import rencontre_controller

app = Flask(__name__)

app.register_blueprint(equipe_controller)
app.register_blueprint(rencontre_controller)



if __name__ == '__main__':
    app.run()
