#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(100), ForeignKey('states.id', ondelete='CASCADE'),
                      nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
