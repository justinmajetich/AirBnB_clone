#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    
    __tablename__ = 'cities'
    
    name = Column(String(128),nullable=False)
    state_id = Column(String(128), ForeignKey("states.id"), nullable=False)
    
    def __init__(self, *args, **kwargs):
        """_summary_
        Initialize City instance
        """
        super().__init__(*args, **kwargs)
  