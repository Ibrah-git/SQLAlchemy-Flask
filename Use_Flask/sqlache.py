### 1. Importation des modules nécessaires

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError

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
    date_inscription = db.Column(db.DateTime, default=datetime.now)

    ### 4. Représentation de l'objet User
    def __repr__(self):
        return f"<User {self.id} {self.nom} {self.prenom} {self.email} {self.age} {self.date_inscription}>"
    
    
    ### 5. Mise en place d'une fonction pour ajouter un utilisateur à la base de données
def ajouter_utilisateur(id,nom, prenom, age, email,date_inscription=None):
    nouvel_utilisateur = User(id=id, nom=nom, prenom=prenom, age=age, email=email, date_inscription=date_inscription)
    db.session.add(nouvel_utilisateur)
    try:
        db.session.commit()
        print(f"Utilisateur {nom} {prenom} ajouté avec succès !")
    except IntegrityError:
        db.session.rollback()
        print(f"Erreur : L'email {email} est déjà utilisé.") 

### 6. Création de la base de données et ajout d'utilisateurs
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crée les tables dans la base de données
        ajouter_utilisateur(1, "Dupont", "Jean", 30, "jean.dupont@example.com")
        ajouter_utilisateur(2, "Durand", "Marie", 25, "marie.durand@example.com")
        ajouter_utilisateur(3, "Martin", "Paul", 28, "paul.martin@example.com")
        ajouter_utilisateur(4, "Dupont", "Sophie", 22, "sophie.dupont@example.com")
        ajouter_utilisateur(5, "Durand", "Luc", 35, "luc.durand@example.com")






