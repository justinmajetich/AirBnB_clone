#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """ Represents a city for a MySQL database.
    """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    places = relationship("Place", backref="cities",
                          cascade="all, delete", passive_deletes=True)
