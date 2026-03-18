from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route('/Bonjour')
def Bonjour():
    return "Bonjouur les amis !" 

@app.route('/user/<name>')
def profil(name):
    return f"Bienvenue sur votre profil {name}!"

@app.route('/article/<int:id>')
def article(id):
    return f"Voici l'article numéro {id} !"


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return "Page de contact !"

@app.route('/ancien')
def ancien():
    return f"Cette page a été déplacée !"

@app.route('/nouveau')
def nouveau():
    return "Bienvenue sur la nouvelle page !"

if __name__ == '__main__':
    app.run(debug=True)