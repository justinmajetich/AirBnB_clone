#!/usr/bin/python3
""" class State  """
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import environ
from models.city import City
from models import storage





class State(BaseModel, Base):
    """ class State """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        from models.engine.db_storage import DBStorage
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):

            City_list = []
            for i in list(storage.all(City).values()):
                if self.id == i.state_id:
                    City_list.append(i)
            return City_list