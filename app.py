from flask import Flask, jsonify
from controllers.test_controller import test_controller  

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Bienvenue sur l'API Euro 2024"}), 200

app.register_blueprint(test_controller)

if __name__ == '__main__':
    app.run(debug=True)  
