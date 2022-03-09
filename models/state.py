#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
import os


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="states",
                          passive_deletes=True,
                          single_parent=True)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """returns a list of all cities identified with a state"""

            from models import storage
            from models import City

            all_objects = storage.all()
            city_list = []
            for key, val in all_objects.items():
                if val.state_id == self.id:
                    city_list.append(val)
            return city_list
