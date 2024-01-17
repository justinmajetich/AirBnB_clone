#!/usr/bin/python3
"""
city module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv
import models


class City(BaseModel, Base):
    """
    City class that inherit from BaseModel
    """
    if models.storageType == "db":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the user instance with given arguments."""
        super().__init__(*args, **kwargs)