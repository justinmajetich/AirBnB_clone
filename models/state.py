#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
import models
# from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """city getter"""
        citlst = []
        for x in models.storage.all(City):
            if getattr(x, "State.id") == self.id:
                citlst.append(x)
        return(citlst)
