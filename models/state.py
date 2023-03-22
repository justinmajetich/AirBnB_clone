#!/usr/bin/python3
""" class State  """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ class State """
    __tablename__ = 'states'

    ##if os.getenv('HBNB_TYPE_STORAGE') == "db":
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
    #else:

        #name = ""
    @property
    def cities(self):
        from models import storage
        from models.city import City
        City_list = []
        for i in storage.all(City).values():
            if self.id == i.state_id:
                City_list.append(i)
        return City_list
