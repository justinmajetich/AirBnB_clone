#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    from sqlalchemy import Column, String, ForeignKey
    from sqlalchemy.orm import relationship

    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="all, delete")
