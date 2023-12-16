#!/usr/bin/python3
"""Defines the City class."""
import models

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
storage_type = getenv("HBNB_TYPE_STORAGE")

class City(BaseModel, Base):
    """Represent a city."""

    __tablename__ = "cities"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""
