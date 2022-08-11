#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name

    __tablename__ = "cities"
<<<<<<< HEAD

    if getenv("HBNB_TYPE_STORAGE") != "db":
        name = ""
        state_id = ""
    else:
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    """
    __tablename__ = "cities"
    name = ""
    state_id = ""
=======
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id", ondelete="CASCADE"),
                      nullable=False)
    places = relationship("Places", cascade="all, delete-orphan", backref="cities")
>>>>>>> jose
