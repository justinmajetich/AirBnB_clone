#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base 
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage_type

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete-orphan');
        base_id = Column(String, ForeignKey('base.id'), nullable=False)

        __mapper_args__ = {
                'polymorphic_identity': 'states',
                'primaryjoin': base_id == BaseModel.id,
                'inherit_condition': base_id == BaseModel.id
                }
    else:
        name = ''

        @property
        def cities(self):
            """
            returns the list of City instances with
            state_id equals to the current State.id
            FileStorage relationship b2n state n city
            """
            from models import storage
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
