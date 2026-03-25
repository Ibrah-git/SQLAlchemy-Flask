from datetime import datetime
import dbm
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship,Mapped, mapped_column
from database import app , db 

class Commande(db.Model):
    __tablename__ = 'Commandes'
    id_commande = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id_papier = db.Column(db.Integer, db.ForeignKey('papiers.id_papier'), nullable=False)
    date_commande = db.Column(db.DateTime, default=datetime.now)
    quantite = db.Column(db.Integer, nullable=False)