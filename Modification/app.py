## 1. Le moteur (Engine) Coeur de la connexion 
from sqlalchemy import create_engine 
import pandas as pd 

engine=create_engine(r'sqlite:///C:/Users/pc/Desktop/Projet/FLASK_INTRO/Architect_flask/modification/produit.db')

with engine.connect() as connection:
    ## Requete simple 
    produit=pd.read_sql_query("SELECT * FROM produits",connection)
    print(produit)
    print("C'est tout bon !")

    # 2ème methode 

    produit2=pd.read_sql_table(
        "produits",
        connection,
        columns=["id_produit","nom_produit","description"]
                              )
    print(produit2)
    print("Affiche pour la deuxieme methode")





