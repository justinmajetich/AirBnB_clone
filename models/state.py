#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Mapped[str] = mapped_column(String(128), nullable=False)
