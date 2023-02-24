#!/usr/bin/python3
#!/usr/bin/python3
""" The state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """
    The class for State
    Attributes:
    name: input name
    """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        name = ""

        @property
        def cities(self):
            cities_dict = models.storage.all(City)
            cities_list = []
            for city in cities_dict.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
    else:
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
