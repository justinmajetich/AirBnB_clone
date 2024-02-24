#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
#vvv to be reimplimented when back to merge
#from .base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

#class User(BaseModel, Base):
class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column('email', String(128), nullable=False)
    password = Column('password', String(128), nullable=False)
    first_name = Column('first_name', String(128))
    last_name = Column('last_name', String(128))

    places = relationship('Place', back_populates='user', cascade='all, delete-orphan')
    reviews = relationship('Review', back_populates='user', cascade='all, delete-orphan')
