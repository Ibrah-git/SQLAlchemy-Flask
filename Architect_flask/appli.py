from datetime import datetime

from database import app , db
from models.users import User
from models.papier import Papier
from models.commande import Commande
from models.production import Production
from models.machine import Machine
from models.maintenance import Maintenance
from datetime import datetime


with app.app_context():

    ### 1.D'abord les ceux qui n'ont pas de foreign key
    db.drop_all()
    db.create_all() 
    user1 = User(nom="Dupont", prenom="Jean", age=30, email="jean.dupont@example.com")
    papier1 = Papier(type_papier="A4", grammage=80, prix_rame=5)
    machine1 = Machine(modèle_machine="Xerox 123", date_achat=datetime(2020, 1, 1), vitesse_production=100)

    ## On les ajoutes et les pousses vers la base de données
    db.session.add(user1)
    db.session.add(papier1)
    db.session.add(machine1)
    db.session.flush()  # Flush pour obtenir les IDs générés avant de les utiliser dans les foreign keys
    
    ### 2.Ajouter ceux qui ont des foreign key
    commande1 = Commande(
        id_user=user1.id,
        id_papier=papier1.id_papier,
        date_commande=datetime.now(),
        quantite=10
    ) 
    db.session.add(commande1)
    db.session.flush()  # Flush pour obtenir l'ID de la commande avant de l'utiliser dans la production

    Production1 = Production(
        id_commande=commande1.id_commande,
        id_machine=machine1.id_machine,
        date_production=datetime.now(),
        dechet=2
    )

    maintenance1 = Maintenance(
        id_machine=machine1.id_machine,
        date_maintenance=datetime.now(),
        type_maintenance="Préventive",
        cout_maintenance=200
    )

    db.session.add(Production1)
    db.session.add(maintenance1)

    db.session.commit() 
    print("Données insérées avec succès !") 





    

    
    



