#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                            cascade="all, delete-orphan")

    @property
    def cities(self):
        """Getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id"""
        from models import storage
        # get all obj from storage
        var = storage.all()
        #initialize empty lists to store city obj & filtered city obj
        lista = []
        result = []
        # iterate through each key replace chr split key to list of str
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[key])
        for elem in lista:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
