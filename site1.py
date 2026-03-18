from flask import Flask 

app = Flask(__name__)

@app.route('/')

def acceuil():
    return "Bienvenue sur mon site web !"

if __name__ == '__main__':
    app.run(debug=True) 