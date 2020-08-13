#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'states'
    name = Column(
        'name',
        String(128),
        nullable=False
    )

    # for dbstorage:
    cities = relationship('City')

    # for filestorage:
    @property
    def cities(self):
        new_dict = {}
    
    #Pendiente hacer la relacion con la llave foranea (cities)