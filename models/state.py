#!/usr/bin/python3
""" State Module for HBNB project """
from typing import Counter
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    link = relationship("City", backref="city", passive_deletes=True)
