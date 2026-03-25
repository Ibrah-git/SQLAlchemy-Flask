from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import (DeclarativeBase, sessionmaker)


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'  # Utilisation d'une base de données SQLite 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app) 


DATABASE8_URL = "sqlite:///Architect_flask.db" 
