#!/usr/bin/python3
'''
    Implementation of the Review class
'''

import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    '''
        Implementation for the Review.
    '''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60),  ForeignKey("users.id"), nullable=False)
    else:
        text = ""
        place_id = ""
        user_id = ""
