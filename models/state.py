#!/usr/bin/python3
""" class State  """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ class State """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    @property
    def cities(self):
        from models import storage
        City_list = []
        for i in list(storage.all(City).values()):
            if self.id == i.state_id:
                City_list.append(i)
        return City_list
