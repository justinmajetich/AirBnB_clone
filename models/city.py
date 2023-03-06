#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.state import State
from models.base_model import Base

class City(BaseModel, Base):
    "Clase City"
    __tablename__='cities'
    name = Column(String(128), nullable = False)
    state_id = Column(String(60), ForeignKey('state.id'), nullable = False)
