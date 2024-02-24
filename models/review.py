#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
#vvv to be reimplimented
#from .base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


#vvv to be reimplimented
#class Review(BaseModel, Base):
class Review(BaseModel):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    place_id = Column('place_id', String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column('user_id', String(60), ForeignKey('users.id'), nullable=False)
    text = Column('text', String(1024), nullable=False)

    place = relationship('Place', back_populates='reviews')
