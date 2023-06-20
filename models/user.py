#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb
import shlex
from sqlalchemy.orm import relationship
from models.place import Place


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="user")
