
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/exemple', methods=['POST'])
def exemple(): 
    # Corps de la requête en JSON {"nom:Alice"}
    data = request.get_json()
    nom = data.get('nom')

    ## Paramètre d'URL : /api/exemple?nom=Alice
    page= request.args.get('page',1 , type=int)
    tri = request.args.get('tri', 'date')

    ### Formulaire HTML : <form action="/api/exemple" method="post"><input name="nom"></form>
    email = request.form.get('email')

    ## En-tête de la requête HTTP : {"Authorization: Bearer token"}
    token = request.headers.get('Authorization')

    return jsonify({'page': page, 'tri':tri , "nom": nom})  

if __name__ == '__main__':
    app.run(debug=True)