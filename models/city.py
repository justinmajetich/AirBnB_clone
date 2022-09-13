#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ Represents a City for MySQL DB, contains state ID and name 
    
    Inherits the BaseModel and Base(from sqlalchemy) and links to the mysql table cities

    Attributes:
      __tablename__(str): name of the MySQL table
      name(sqlalchemy String): name of the City
      state_id(sqlalchemy String): state_id of the City
    """
    if models.storage_type == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        def __init__(self, state_id = "", name = ""):
            """ if storage type is FileStorage instantiate the values """
            self.state_id = state_id
            self.name = name
            super().__init__()
