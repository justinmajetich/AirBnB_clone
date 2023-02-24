#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import column, String, ForeignKey 


class Review(BaseModel, Base):
    """ 
    Review classto store review information
    """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
         place_id = column(String(60), ForeignKey("places.id"), nullable=False)
         user_id = column(String(60), ForeignKey("user.id"), nullable=False)
         text = column(String(1024), nullable=False)
    else:
         place_id=""
         user_id=""
         text=""

