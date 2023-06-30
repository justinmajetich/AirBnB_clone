#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base


class State(BaseModel, Base):
    """ State class """
   class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if models.storage_type == 'db':
        cities = relationship("City", cascade="all, delete-orphan", backref="state")
    else:
        @property
        def cities(self):
            from models import storage
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list


