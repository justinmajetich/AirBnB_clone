#!/usr/bin/python3
""" State Module for HBNB project """
from .base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column('name', String(128), nullable=False)

    cities = relationship('City', back_populates='state', cascade='all, delete-orphan')

    # @property
    # def cities(self):
    #     return [city for city in City.query.filter_by(state_id=self.id).all()]
