#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Columns, String, Foreignkey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    state_id = Column(String=(60), nullable=False)
    name = Column(String=(128), ForeignKey('state_id'), nullable=False)
