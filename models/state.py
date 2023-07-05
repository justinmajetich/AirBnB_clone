#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete, delete-orphan")

else:

    class State(BaseModel):
        """File Storage State"""
        name = ""

        @property
        def cities(self):
            """Returns a list of cities equal to their state ID"""
            from models import storage
            list_cities = []
            for key, i in storage.all(City).items():
                if i.state_id == self.id:
                    list_cities.append(i)
            return list_cities