#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, String
=======
from sqlalchemy import Column, VARCHAR
from sqlalchemy.orm import relationship

>>>>>>> destiny

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
<<<<<<< HEAD
    __tablename__ = 'users'
    
    
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    
    def __init__(self, *args, **kwargs):
        """Initializes User instance"""
        super().__init__(*args, **kwargs)
=======
    __tablename__ =  'users'
    email = Column(VARCHAR(128), nullable=False)
    password = Column(VARCHAR(128), nullable=False)
    first_name = Column(VARCHAR(128), nullable=False)
    last_name = Column(VARCHAR(128), nullable=False)

    places = relationship("Place", backref='user', cascade="all, delete")
    reviews = relationship("Review", backref='user', cascade="all, delete")
>>>>>>> destiny
