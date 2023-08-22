#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from models.place import Place
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, inherit from BaseModel, and Base
    Attributes:
        name: string(128)
        state_id: string(60), foreign key
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    places = relationship('Place', cascade='all, delete, delete-orphan',
                          backref='cities')
