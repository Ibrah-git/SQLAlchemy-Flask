
import os 
from datetime import datetime 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from database import app,db 

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


# Definition de la classe 

class Category(db.Model):
    """ Categories de produits"""

    __tablename__="categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 

    # Relations 
    #produits = relationship("Product",back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name=’{self.name}’)>"

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Ajout des categories 
        categorie1 = Category(name="A",description="grand",is_active=True)
        categorie2 = Category(name="B",description="Moyen",is_active=False)
        categorie3 = Category(name="D",description="petit",is_active=True)
        categorie4 = Category(name="C",description="grand",is_active=False)
        categorie5 = Category(name="E",description="petit",is_active=False)

        db.session.add_all([categorie1,categorie2,categorie3,categorie4,categorie5])
        db.session.commit()









   
