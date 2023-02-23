#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__= "users"
    email = Column(String(128), nullable=False)
    password = ''
    first_name = ''
    last_name = ''
    places = relationship("Place", backref='user')
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
