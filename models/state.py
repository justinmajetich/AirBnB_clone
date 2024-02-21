#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage


class State(BaseModel, Base):
    """Creates a State object"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        """Getter attribute that returns a list of city instances
            For use with Filestorage
        """
        storage = FileStorage()
        filtered_cities = [(city) for city in storage.all()
                           if city.state_id == city.id]

        return filtered_cities
