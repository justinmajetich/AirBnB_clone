#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Name of table in database to link to """
    __tablename__ = 'reviews'

    """ these classes """
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
