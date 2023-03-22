#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Mapped[str] = mapped_column(String(128), nullable=False)
    state_id = Mapped[int] = mapped_column(ForeignKey("states.id"), nullable=False)
