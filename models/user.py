#!/usr/bin/python3
""" User Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import uuid

class User(BaseModel, Base):
    """ User class """
    __tablename__ = 'users'
    id = Column(String(60), primary_key=True, nullable=False, default=uuid.uuid4().hex)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
