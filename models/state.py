#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Colomn, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel):
    """Defines attributes/method for the State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.environ.get('HBNB_TYPE_STORGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """Getter attribute for cities that returns a list of
            city instances"""
            city_list = [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
            return city_list
