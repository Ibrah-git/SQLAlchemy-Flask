
import os 
from datetime import datetime 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from database import app,db 

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func



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
 


# 3 Définition du modèle de données pour les produits
class Product(db.Model):
    """Produit avec cl etrangère"""
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Cl trangre
    category_id = Column(Integer, ForeignKey('categories.id'))

    # Relations 
    #category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id}, name=’{self.name}’, price={self.price})>"
        
        
# 4 Création de la base de données et des tables
if __name__ == '__main__':
    with app.app_context():
        #db.drop_all()
        db.create_all()  # Crée les tables dans la base de données
        # 5 Ajout d'un produit d'exemple
        produit1 = Product(name="Papier A4", price=5.0, stock=16, description="Rame de papier A4", is_active=True)
        produit2 = Product(name="Papier A3", price=7.0, stock=10, description="Rame de papier A3", is_active=True)
        produit3 = Product(name="Papier B1", price=5.56, stock=9, description="Rame de papier B1", is_active=False)
        produit4 = Product(name="Papier A15", price=19.0, stock=106, description="Rame de papier A15", is_active=True)
        produit5 = Product(name="Papier A49", price=12.0, stock=16, description="Rame de papier A49", is_active=False)
        
        

        db.session.add(produit1)
        db.session.add(produit2)
        db.session.add(produit3)
        db.session.add(produit4)
        db.session.add(produit5)
        db.session.commit()
        
        print("Base de données Produits.db créée et produit ajouté avec succès !")
        print("Les nouveaux éléments ont été rajoutés")

