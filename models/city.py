#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.place import Place


class City(BaseModel):
    """ The city class, contains state ID and name """
    Attributes:
        state_id: The state id
        name: input name
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        name = ""
        state_id = ""
