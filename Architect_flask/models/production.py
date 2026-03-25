
from datetime import datetime
import dbm
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship,Mapped, mapped_column
from database import app , db 

class Production(db.Model):
    __tablename__ = 'productions'
    id_production = db.Column(db.Integer, primary_key=True)
    id_commande = db.Column(db.Integer, db.ForeignKey('Commandes.id_commande'), nullable=False)
    id_machine = db.Column(db.Integer, db.ForeignKey('Machines.id_machine'), nullable=False)
    date_production = db.Column(db.DateTime, default=datetime.now)
    dechet = db.Column(db.Integer, nullable=False) 
      
