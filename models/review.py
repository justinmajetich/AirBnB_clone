#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import column, String, ForeignKey 


class Review(BaseModel, Base):
    """ 
    Review classto store review information
    """
    __table__name = 'reviews'
    
    place_id = column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = column(String(60), ForeignKey("user.id"), nullable=False)
    text = column(String(1024), nullable=False)
    

