
from datetime import datetime
import dbm
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship,Mapped, mapped_column
from database import app , db 
 
class Machine(db.Model):
    __tablename__ = 'Machines'
    id_machine = db.Column(db.Integer, primary_key=True)
    modèle_machine = db.Column(db.String(100), nullable=False)
    date_achat = db.Column(db.DateTime, default=datetime.now)
    vitesse_production = db.Column(db.Integer, nullable=False) 