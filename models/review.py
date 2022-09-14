#!/usr/bin/python3
""" Review module for the HBNB project """
# Added sqlalchemy module
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Float

# class review
class Review(BaseModel, Base):
    """ This is the class for Review
    Attributes:
    place_id = place id
    user_id = user id
    text = review description
    """
# I added the class attribute __tablename__ and also made sure the properties aren't null
__tablename__ = "reviews"
text = Column(String(1024), nullable=False)
place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
