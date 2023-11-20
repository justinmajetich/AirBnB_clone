#!/usr/bin/env python3
""" State Module for HBNB project """
import uuid
from models.base_model import BaseModel, Base, id_generator
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    id = Column(String(60), primary_key=True, default=id_generator)
    name = Column(String(128), nullable=False, unique=True)

    def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        self.name = kwargs['name']
