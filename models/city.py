#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'  # Table name is 'cities'

    name = Column(String(128), nullable=False)  # Column for city name, not nullable
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)  # Column for state_id, foreign key to states.id

    # Establish a relationship with the State model
    state = relationship("State", back_populates="cities")
