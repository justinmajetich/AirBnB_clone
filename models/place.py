#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
import os


if os.environ.get("HBNB_TYPE_STORAGE") == 'db':
    place_amenity = Table("place_amenity", Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 back_populates="place_amenities",
                                 viewonly=False)
    else:
        from models import storage

        @property
        def reviews(self, place_id):
            """method to return a list of reviews for a place"""

            all_objects = storage.all()
            rev_list = []
            for key, val in all_objects.items():
                class_name = (key.split('.', 1))[0]
                place_id = val.place_id
                if class_name == "Review" and place_id == self.id:
                    rev_list.append(val)
            return rev_list

        @property
        def amenities(self):
            """method to get amenity instances linked to this place"""

            all_objects = storage.all()
            amen_list = []
            for key, val in all_objects.items():
                class_name = (key.split('.', 1))[0]
                amen_id = val.amenity_id
                if class_name == "Amenity" and amen_id == self.id:
                    amen_list.append(val)
            return amen_list

        @amenities.setter
        def append(self, amenity_obj):
            """method to add an amenity to list of amenities"""

            if amenity_obj.__class__.__name__ == "Amenity":
                amenity_ids.append(amenity_obj.id)
