#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Columns, String, Foreignkey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    state_id = Column(String=(60), nullable=False)
    name = Column(String=(128), ForeignKey('state_id'), nullable=False)

    """City class for storing city information"""

    if models.storage_type == 'db':
        places = relationship("Place", cascade="all, delete", back_populates="city")
    else:
        @property
        def places(self):
            from models import storage
            from models.place import Place
            all_places = storage.all(Place)
            return [place for place in all_places.values() if place.city_id == self.id]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
