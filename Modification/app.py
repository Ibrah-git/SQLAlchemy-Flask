## 1. Le moteur (Engine) Coeur de la connexion 
from sqlalchemy import create_engine 
import pandas as pd 
import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(os.path.join(basedir, 'database.db'))
engine=create_engine(r'sqlite:///' + os.path.join(basedir, 'database.db'))

with engine.connect() as connection:
    ## Requete simple 
    produit =pd.read_sql_query("SELECT * FROM product ", connection)
    categorie = pd.read_sql_query("SELECT * FROM categories", connection)
    print(categorie)
    print("Pour les categorie c'est ok !")
    print(produit)
    print("C'est tout bon !")






