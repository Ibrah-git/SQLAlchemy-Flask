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
    ### Table "Usesr"
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer , primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_inscription = db.Column(db.DateTime, default=datetime.now)
    # Représentation de l'objet pour faciliter le débogage
    def __repr__(self):
        return f"<User {self.nom} {self.prenom} - {self.email}>"


    ### Table Papier 

class Papier(db.Model):
    __tablename__ = 'papiers'
    id_papier = db.Column(db.Integer, primary_key=True)
    type_papier = db.Column(db.String(200), nullable=False)
    grammage = db.Column(db.String(100), nullable=False)
    prix_rame = db.Column(db.Integer, nullable=False)
    # Représentation de l'objet pour faciliter le débogage
    def __repr__(self):
        return f"<Papier {self.type_papier} - {self.grammage} - {self.prix_rame}€>"
    
    ### Table Commandes
class Commande(db.Model):
    __tablename__ = 'Commandes'
    id_commande = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id_papier = db.Column(db.Integer, db.ForeignKey('papiers.id_papier'), nullable=False)
    date_commande = db.Column(db.DateTime, default=datetime.now)
    quantite = db.Column(db.Integer, nullable=False) 
    # Representation de l'objet 
    def __repr__(self):
        return f"<Commande {self.id_commande} - User ID: {self.id_user} - Papier ID: {self.id_papier} - Quantité: {self.quantite}>"

    ### Table de Production 
class Production(db.Model):
    __tablename__ = 'productions'
    id_production = db.Column(db.Integer, primary_key=True)
    id_commande = db.Column(db.Integer, db.ForeignKey('Commandes.id_commande'), nullable=False)
    id_machine = db.Column(db.Integer, db.ForeignKey('Machines.id_machine'), nullable=False)
    date_production = db.Column(db.DateTime, default=datetime.now)
    dechet = db.Column(db.Integer, nullable=False)
    # Representation de l'objet
    def __repr__(self):
        return f"<Production {self.id_production} - Commande ID: {self.id_commande} - Machine ID: {self.id_machine} - Déchet: {self.dechet}>"

    ### Table des Machines
class Machine(db.Model):
    __tablename__ = 'Machines'
    id_machine = db.Column(db.Integer, primary_key=True)
    modèle_machine = db.Column(db.String(100), nullable=False)
    date_achat = db.Column(db.DateTime, default=datetime.now)
    vitesse_production = db.Column(db.Integer, nullable=False)
    # Representation de l'objet
    def __repr__(self):
        return f"<Machine {self.modèle_machine} - Date d'achat: {self.date_achat} - Vitesse de production: {self.vitesse_production}>"

    #### Table de Maintenance
class Maintenance(db.Model):
    __tablename__ = 'Maintenances'
    id_maintenance = db.Column(db.Integer, primary_key=True)
    id_machine = db.Column(db.Integer, db.ForeignKey('Machines.id_machine'), nullable=False)
    date_maintenance = db.Column(db.DateTime, default=datetime.now)
    type_maintenance = db.Column(db.String(100), nullable=False)
    cout_maintenance = db.Column(db.Integer, nullable=False)
    # Representation de l'objet
    def __repr__(self):
        return f"<Maintenance {self.id_maintenance} - Machine ID: {self.id_machine} - Type: {self.type_maintenance} - Coût: {self.cout_maintenance}>"

    

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

def ajouter_papier(id_papier, type_papier, grammage, prix_rame):
    nouveau_papier = Papier(id_papier=id_papier, type_papier=type_papier, grammage=grammage, prix_rame=prix_rame)
    db.session.add(nouveau_papier)
    try:
        db.session.commit()
        print(f"Papier {type_papier} ajouté avec succès !")
    except IntegrityError:
        db.session.rollback()
        print(f"Erreur : Le papier {type_papier} est déjà utilisé.")

def ajouter_commande(id_commande, id_user, id_papier, quantite, date_commande=None):
    nouvelle_commande = Commande(id_commande=id_commande, id_user=id_user, id_papier=id_papier, date_commande=date_commande or datetime.now(), quantite=quantite)
    db.session.add(nouvelle_commande)
    try:
        db.session.commit()
        print(f"Commande {id_commande} ajoutée avec succès !")
    except IntegrityError:
        db.session.rollback()
        print(f"Erreur : La commande {id_commande} est déjà utilisée.")

def ajouter_production(id_production, id_commande, id_machine, dechet):
    nouvelle_production = Production(id_production=id_production, id_commande=id_commande, id_machine=id_machine, dechet=dechet)
    db.session.add(nouvelle_production)
    try:
        db.session.commit()
        print(f"Production {id_production} ajoutée avec succès !")
    except IntegrityError:
        db.session.rollback()
        print(f"Erreur : La production {id_production} est déjà utilisée.")

def ajouter_machine(id_machine, modèle_machine, date_achat=None, vitesse_production=None):
    nouvelle_machine = Machine(id_machine=id_machine, modèle_machine=modèle_machine, date_achat=date_achat, vitesse_production=vitesse_production)
    db.session.add(nouvelle_machine)
    try:
        db.session.commit()
        print(f"Machine {modèle_machine} ajoutée avec succès !")
    except IntegrityError:
        db.session.rollback()
        print(f"Erreur : La machine {modèle_machine} est déjà utilisée.")

def ajouter_maintenance(id_maintenance, id_machine, date_maintenance, type_maintenance, cout_maintenance):
    nouvelle_maintenance = Maintenance(id_maintenance=id_maintenance, id_machine=id_machine, date_maintenance=date_maintenance, type_maintenance=type_maintenance, cout_maintenance=cout_maintenance)
    db.session.add(nouvelle_maintenance)
    try:
        db.session.commit()
        print(f"Maintenance {id_maintenance} ajoutée avec succès !")
    except IntegrityError:
        db.session.rollback()
        print(f"Erreur : La maintenance {id_maintenance} est déjà utilisée.")

### 6. Création de la base de données et ajout d'utilisateurs
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crée les tables dans la base de données
        ### 1.D'abord les ceux qui n'ont pas de foreign key
        ajouter_utilisateur(1, "Dupont", "Jean", 30, "jean.dupont@example.com")
        ajouter_utilisateur(2, "Durand", "Marie", 25, "marie.durand@example.com")
        ajouter_utilisateur(3, "Martin", "Paul", 28, "paul.martin@example.com")
        ajouter_utilisateur(4, "Dupont", "Sophie", 22, "sophie.dupont@example.com")
        ajouter_utilisateur(5, "Durand", "Luc", 35, "luc.durand@example.com")
        ajouter_utilisateur(6, "Martin", "Claire", 27, "claire.martin@example.com")
        ajouter_utilisateur(7, "Ibrahim", "Ahmed", 32, "ahmed.ibrahim@example.com")
        ajouter_utilisateur(8, "Nguyen", "Thi", 29, "thi.nguyen@example.com")
        ajouter_utilisateur(9, "Garcia", "Carlos", 31, "carlos.garcia@example.com")
        ajouter_utilisateur(10, "Smith", "John", 26, "john.smith@example.com")
        ajouter_papier(1, "Papier A4", "80g/m²", 5)
        ajouter_papier(2, "Papier A3", "100g/m²", 10)
        ajouter_papier(3, "Papier recyclé", "90g/m²", 7)
        ajouter_papier(4, "Papier photo", "200g/m²", 15)
        ajouter_papier(5, "Papier cartonné", "300g/m²", 20)
        ajouter_papier(6, "Papier kraft", "120g/m²", 8)
        ajouter_papier(7, "Papier calque", "60g/m²", 6)
        ajouter_papier(8, "Papier autocollant", "150g/m²", 12)
        ajouter_papier(9, "Papier sulfurisé", "50g/m² ", 4)
        ajouter_papier(10, "Papier aluminium", "200g/m²", 18)
        ajouter_machine(1, "Imprimante HP", date_achat=datetime(2020, 5, 15), vitesse_production=100)
        ajouter_machine(2, "Presse à imprimer", date_achat=datetime(2019, 3, 10), vitesse_production=200)
        ajouter_machine(3, "Machine de découpe", date_achat=datetime(2021, 7, 20), vitesse_production=150)
        ajouter_machine(4, "Machine de pliage", date_achat=datetime(2020, 11, 5), vitesse_production=120)
        ajouter_machine(5, "Machine de reliure", date_achat=datetime(2018, 2, 25), vitesse_production=80)
        ajouter_machine(6, "Machine de finition", date_achat=datetime(2021, 1, 30), vitesse_production=90)
        ajouter_machine(7, "Machine de contrôle qualité", date_achat=datetime(2019, 9, 12), vitesse_production=110)
        ajouter_machine(8, "Machine de stockage", date_achat=datetime(2020, 6, 18), vitesse_production=70)
        ajouter_machine(9, "Machine de transport", date_achat=datetime(2021, 4, 22), vitesse_production=60)
        ajouter_machine(10, "Machine de maintenance", date_achat=datetime(2018, 12, 1), vitesse_production=50)

        ## 2. Ensuite les éléments dependant des foreign key
        ajouter_commande(1, 1, 1, 10)
        ajouter_commande(2, 2, 2, 20)
        ajouter_commande(3, 3, 3, 30)
        ajouter_commande(4, 4, 4, 40)
        ajouter_commande(5, 5, 5, 50)
        ajouter_commande(6, 6, 6, 60)
        ajouter_commande(7, 7, 7, 70)
        ajouter_commande(8, 8, 8, 80)
        ajouter_commande(9, 9, 9, 90)
        ajouter_commande(10, 10, 10, 100)
        ajouter_production(1, 1, 1, 2)
        ajouter_production(2, 2, 2, 3)
        ajouter_production(3, 3, 3, 1)
        ajouter_production(4, 4, 4, 4)
        ajouter_production(5, 5, 5, 0)
        ajouter_production(6, 6, 6, 5)
        ajouter_production(7, 7, 7, 2)
        ajouter_production(8, 8, 8, 3)
        ajouter_production(9, 9, 9, 1)
        ajouter_production(10, 10, 10, 4)
        ajouter_maintenance(1, 1, datetime(2021, 6, 15), "Réparation", 200)
        ajouter_maintenance(2, 2, datetime(2021, 7, 20), "Entretien", 150)
        ajouter_maintenance(3, 3, datetime(2021, 8, 25), "Réparation", 300)
        ajouter_maintenance(4, 4, datetime(2021, 9, 30), "Entretien", 100)
        ajouter_maintenance(5, 5, datetime(2021, 10, 5), "Réparation", 250)
        ajouter_maintenance(6, 6, datetime(2021, 11, 10), "Entretien", 180)
        ajouter_maintenance(7, 7, datetime(2021, 12, 15), "Réparation", 220)
        ajouter_maintenance(8, 8, datetime(2022, 1, 20), "Entretien", 130)
        ajouter_maintenance(9, 9, datetime(2022, 2, 25), "Réparation", 270)
        ajouter_maintenance(10, 10, datetime(2022, 3, 30), "Entretien", 160)    
        ajouter_maintenance(11, 1, datetime(2022, 4, 5), "Réparation", 210)
        ajouter_maintenance(12, 2, datetime(2022, 5, 10), "Entretien", 140) 


    



