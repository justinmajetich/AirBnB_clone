#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new City"""
        super().__init__(*args, **kwargs)
    places = relationship("Place", backref="city")

    if models.storage_type != "db":
        @property
        def places(self):
            """getter for places that return
            a list of place instance equale to
            curent city id
            """
            list_place = []
            all_inst_p = models.storage.all(Place)
            for value in all_inst_p.values():
                if value.city_id == self.id:
                    list_place.append(value)
            return list_place
