#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    '''
    Definition of the User class
    '''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user",
                              cascade="delete")
        reviews = relationship("Review", cascade="delete", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
