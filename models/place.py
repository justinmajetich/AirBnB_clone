#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")
    metadata = Base.metadata
    place_amenity = Table("place_amenity", metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False, backref="places")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """ getter attriute for reviews"""
            from models import storage
            from models.review import Review
            r_list = []
            for r in list(storage.all(Review).values()):
                if r.state_id == self.id:
                    r_list.append(r)
            return r_list

    @property
    def amenities(self):
        """returns list of Amenity instances based on amenity_ids"""
        from models import storage
        from models.amenity import Amenity
        r_list = []
        for r in list(storage.all(Amenity).values()):
            if r.amenity_ids == self.id:
                r_list.append(r)
        return r_list

    @amenities.setter
    def amenities(self, aob):
        """APPEND DEZ FOES"""
        from models.amenity import Amenity
        if type(aob) is not Amenity:
            return
        else:
            amenity_ids.append(aob.id)
