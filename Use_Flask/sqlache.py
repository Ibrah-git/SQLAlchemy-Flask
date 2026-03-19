### 1. Importation des modules nécessaires

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

### 2. Configuration de l'application Flask et de la base de données

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'  # Utilisation d'une base de données SQLite 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app) 
### 3. Définition du modèle de données

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer , primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_inscription = db.Column(db.DateTime, default=datetime.utcnow)

    ### 4. Représentation de l'objet User
    def __repr__(self):
        return f"<User {self.id} {self.nom} {self.prenom} {self.email} {self.age} {self.date_inscription}>"
    
### 5. Création de la base de données et des tables
with app.app_context():

    db.create_all()  # Crée les tables dans la base de données

    ## Création d'un nouvel utilisateur
    new_user = User(nom="Doe", prenom="John", age=30, email="john.doe@example.com", date_inscription=datetime.utcnow())
    print(f"Avant l'ajout : {new_user}")
    db.session.add(new_user)
    db.session.commit()
    print(f"Après l'ajout : {new_user}") 
