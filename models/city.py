#!/usr/bin/python3
"""
City Module for HBNB project
"""
import models
from models.place import Place
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    The city class, contains state ID and name
    """
    __tablename__ = "cities"

    if models.engine_type == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        name = ""
        state_id = ""
