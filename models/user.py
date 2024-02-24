#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models


if models.env_stroage == 'db':
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", back_populates="user",
                              cascade="all, delete, save-update")
        reviews = relationship("Review", backref="user",
                               cascade='all, delete, save-update')

else:
    class User(BaseModel):
        """This class defines a user by various attributes"""
        email = ""
        password = ""
        first_name = ""
        last_name = ""
