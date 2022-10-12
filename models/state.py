#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel, Base):
    """ State class """
    name = ""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City")

    @property
    def cities(self):
        """ Getter method to return the list of city instances
            from File storage
        """
        myList = []
        d = storage.all()
        for obj_name, obj_dict in d.items():
            if str(obj_name).startswith("City") and\
                    "state_id" in dict(obj_dict).keys() and\
                    dict(obj_dict).get("state_id") == self.id:
                myList.append(obj_dict)
        return myList
