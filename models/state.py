#!/usr/bin/env python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states' #NEW
    name = Column(String(128), nullable=False) #NEW
    cities = relationship("City", cascade="all, delete", backref='state') #NEW

    @property #NEW
    def cities(self): #NEW
        from models import storage #NEW
        from models.city import City #NEW
        temp = [] #NEW
        dictio = storage.all(City) #NEW
        for value in dictio.values(): #NEW
            if value.state_id == self.id: #NEW
                temp.append(value) #NEW
        return temp #NEW
