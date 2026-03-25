from datetime import datetime
import dbm
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship,Mapped, mapped_column
from database import app , db 


class Maintenance(db.Model):
    __tablename__ = 'Maintenances'
    id_maintenance = db.Column(db.Integer, primary_key=True)
    id_machine = db.Column(db.Integer, db.ForeignKey('Machines.id_machine'), nullable=False)
    date_maintenance = db.Column(db.DateTime, default=datetime.now)
    type_maintenance = db.Column(db.String(100), nullable=False)
    cout_maintenance = db.Column(db.Integer, nullable=False)