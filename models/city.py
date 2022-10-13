#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    state = relationship("State", cascade="all, delete-orphan")
    places = relationship("Place", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """ Constructor method to initialize user instances

        Args:
            args: list of arguments
        Kwargs:
            key/value dictionary of arguments
        """
        super().__init__(args, kwargs)
