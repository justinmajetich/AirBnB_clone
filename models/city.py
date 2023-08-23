#!/usr/bin/python3
"""
City Module for HBNB project
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    The city class, contains state ID and name
    """
    from models.place import Place

    __tablename__ = "cities"

    if models.engine_type == "db":
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
#        places = relationship("Place", backref="cities")
    else:
        name = ""
        state_id = ""
