#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class:

    Inherits from SQLAlchemy Base and links to the cities table.

    Attributes:
        __tablename__ (str): The name of the table to use.
        name (sqlalchemy String): The name of the City.
        state_id (sqlalchemy String): The state id of the City.
        places (sqlalchemy relaationship): The Cities-Places relation.
    """

    __tablename__ = 'cities'
    name = Column(String(128),
                  nullable=False)
    state_id = Column(String(60),
                      ForeignKey('states.id'),
                      nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="delete")
