#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from models import storage


class Place(BaseModel, Base):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False,)
    user_id = Column(String(60), ForeignKey("users.id", nullable=False))
    name = Column(String(128), nullable=False)
    descripion = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(float, nullable=False)
    longitude = Column(float, nullable=False)
    user = relationship("User", cascade="all, delete")
    cities = relationship("City", cascade="all, delete")
    reviews = relationship("Review", cascade="all, delete")
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id",
                                            primary_key=True,
                                            nullable=False)),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id",
                                            primary_key=True,
                                            nullable=False)))
    place_amenity = relationship("Amenity",
                                 back_populates="place_amenities",
                                 cascade="all, delete")
    amenities = relationship("Amenity",
                             secondary=association_table,
                             back_populates="place_amenity",
                             viewonly=False)

    @property
    def reviews(self):
        """ Getter method to return the list of Review instances
            from File storage
        """
        myList = []
        d = storage.all()
        for obj_name, obj_dict in d.items():
            if str(obj_name).startswith("Review") and\
                    "state_id" in dict(obj_dict).keys() and\
                    dict(obj_dict).get("place_id") == self.id:
                myList.append(obj_dict)
        return myList

    @property
    def amenities(self):
        """ Getter method to return the list of Amenity instances
            from File storage
        """
        myList = []
        d = storage.all()
        for obj_name, obj_dict in d.items():
            if str(obj_name).startswith("Amenity") and\
                    self.name in dict(obj_dict).keys() and\
                    dict(obj_dict).get("id") in self.amenity_ids:
                myList.append(obj_dict)
        return myList

    @amenities.setter
    def amenities(self):
        """ Setter method handling append method for adding an Amenity.id
            to the attribute amenity_ids
        """
        myList = []
        d = storage.all()
        for obj_name, obj_dict in d.items():
            if str(obj_name).startswith("Amenity") and\
                    dict(obj_dict).get("id") in dict(
                    Base.metadata.tables).get(
                    "place_amenity").columns.amenity_id:
                myList.append(obj_dict)
        self.amenity_ids = list(set(self.amenity_ids.extend(myList)))
