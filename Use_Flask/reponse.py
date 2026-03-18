
from flask import Flask, jsonify , make_response

### Reponse JSON ( code 200 par defaut)
app = Flask(__name__)

@app.route('/api/ping')
def ping():
    data = {"status": "ok"}

# Code de status personnalisé
@app.route('/api/ressource', methods=['POST'])
def creer_ressource():
    return jsonify({"id": 42}), 201

### Gestion des erreurs globales
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Ressource non trouvée"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Erreur interne du serveur"}), 500

if __name__ == '__main__':
    app.run(debug=True) 