#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    state_id = Column(String(128), ForeignKey("state.id"), nullable=False)
    name = Column(String(60), nullable=False)
