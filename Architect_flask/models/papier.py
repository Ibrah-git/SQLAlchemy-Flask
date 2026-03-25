
from datetime import datetime
import dbm
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship,Mapped, mapped_column
from database import app , db 

class Papier(db.Model):
    __tablename__ = 'papiers'
    id_papier = db.Column(db.Integer, primary_key=True)
    type_papier = db.Column(db.String(200), nullable=False)
    grammage = db.Column(db.String(100), nullable=False)
    prix_rame = db.Column(db.Integer, nullable=False) 

   