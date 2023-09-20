#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey, Float
from sqlalchemy.orm import relationship

place_amenity = Table("place_amenity", Base.metadata, 
                               Column('place_id', ForeignKey('place.id'), String(60), 
                                      nullable=False, PrimaryKey=True),
                                Column('amenities_id', ForeignKey('amenities.id'), String(60), 
                                       nullable=False, PrimaryKey=True)
                                       ) 
                                
class Amenity(BaseModel, Base):
    name = ""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", "Amenities")
