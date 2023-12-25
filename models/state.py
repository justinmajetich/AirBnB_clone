#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(City, backref="state", cascade="all, delete")

    @property
    def cities(self):
        """
        returns the list of City instances with state_id
        equals to the current State.id =>
        It will be the FileStorage relationship between State and City
        """
        from models import storage
        instances = []
        for obj in storage.all(City).values():
            if self.id == obj.state_id:
                instances.append(obj)
        return instances
