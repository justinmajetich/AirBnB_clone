#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel

s = "HBNB_TYPE_STORAGE"
if s in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    class Amenity(BaseModel, Base):
        """
        This is the state class
        """
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)

        def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for k, v in kwargs.items():
                setattr(self, k, v)
else:
    class Amenity(BaseModel):
        """This is the class for Amenity
        Attributes:
            name: input name
        """
        name = ""
