#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref

__tablename__= 'users'

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship(
        cascade="all,delete",
        backref=backref("user", cascade="all,delete"),
        passive_deletes=True,
        single_parent=True
    )
