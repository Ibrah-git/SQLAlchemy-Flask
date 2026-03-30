## 1. Le moteur (Engine) Coeur de la connexion 
from sqlalchemy import create_engine 
import pandas as pd 
import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(os.path.join(basedir, 'database.db'))
engine=create_engine(r'sqlite:///' + os.path.join(basedir, 'database.db'))

with engine.connect() as connection:
    ## Requete simple 
    df =pd.read_sql_query("SELECT * FROM product ", connection)
    ab = pd.read_sql_query("SELECT * FROM categories", connection)
    #print(df)
    #print("c'est ok")
    #print(ab)
    #print("good")
    ## Analyse de donné avance avec pandas 
    liste=df.groupby("name")["price"].sum()
    print(liste)

    # 5. Statistiques descriptives 
    stats=ab.describe()
    print(stats)
    print("OK !")
    
   



  
    






