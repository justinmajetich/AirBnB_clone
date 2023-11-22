#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(128), ForeignKey("states.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        filtered_kwargs = {k: v for k, v in kwargs.items() if hasattr(self, k) or k == "id"}
        super().__init__(*args, **filtered_kwargs)
        self.name = kwargs.get("name", "")
        self.state_id = kwargs.get("state_id", "")
