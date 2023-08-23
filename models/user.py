#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        
        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')

        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')

        def __init__(self, **kwargs):
            self.id = str(uuid4())
            for key, value in kwargs.items():
                setattr(self, key, value)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
