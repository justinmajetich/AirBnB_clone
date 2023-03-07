#!/usr/bin/python3
""" City module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """ City class """

    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    places = relationship("Place", backref="cities", cascade="all, delete")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def places(self):
            """getter method to retrieve all Places instances related to the city"""
            from models import storage
            places_list = []
            for place in storage.all("Place").values():
                if place.city_id == self.id:
                    places_list.append(place)
            return places_list

    def __init__(self, *args, **kwargs):
        """initializes city"""
        if os.getenv("HBNB_TYPE_STORAGE") != "db":
            self.name = ""
            self.state_id = ""
        super().__init__(*args, **kwargs)