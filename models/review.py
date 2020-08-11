#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""

"""
Review inherits from BaseModel and Base (respect the order)
Add or replace in the class Review:
class attribute __tablename__
        represents the table name, reviews
class attribute text
        represents a column containing a string (1024 characters)
        can’t be null
class attribute place_id
        represents a column containing a string (60 characters)
        can’t be null
        is a foreign key to places.id
class attribute user_id
        represents a column containing a string (60 characters)
        can’t be null
        is a foreign key to users.id
"""

"""class USER -- class attribute reviews must represent a relationship with the class Review. If the User object is deleted, all linked Review objects must be automatically deleted. Also, the reference from a Review object to his User should be named user


class PLACE -- for DBStorage: class attribute reviews must represent a relationship with the class Review. If the Place object is deleted, all linked Review objects must be automatically deleted. Also, the reference from a Review object to his Place should be named place
for FileStorage: getter attribute reviews that returns the list of Review instances with place_id equals to the current Place.id => It will be the FileStorage relationship between Place and Review
"""
