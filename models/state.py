#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from os import getenv
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import uuid  # Import the uuid module

<<<<<<< HEAD
class State(BaseModel):
    """ State class """
    name = ""
=======

class State(BaseModel, Base):
    """ State class
    Attributes:
        __tablename__: states to store in table
        name: name of state
        cities: state-city relationship
        """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                          cascade='all, delete, delete-orphan')
    
     def __init__(self, *args, **kwargs):
        """ Initialize State class """
        super().__init__(*args, **kwargs)

        # Generate the 'id' attribute if it doesn't exist
        if not hasattr(self, 'id'):
            self.id = str(uuid.uuid4())

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            related_city = []
            for city in list(models.storage.all(City).values()):
                if city.state_id = self.id:
                    related_city.append(city)
            return related_city
>>>>>>> a6d7bd68dbe206547cb3f0b3931e52d67897ecfa
