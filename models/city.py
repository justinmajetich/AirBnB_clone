#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class City(BaseModel, Base):
    """Name of table in database to link to"""
    __tablename__ = "cities"

    """This class defines a user by name & state_id attributes"""
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    """Check if env variable is db(sql), if so create rel w/ place"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        places = relationship('Place', cascade='all, delete-orphan', backref='state')
        """If env variable is not db(sql), its FileStorage"""
    else:
        @property
        def places(self):
            from models import storage
            return [place for place in storage.all(Place).values() if place.city_id == self.id]