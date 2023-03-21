#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
#from models.review import Review
from sqlalchemy.orm import relationship
import os
#from models.amenity import Amenity
place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id"),
            primary_key=True,
            nullable=False
        ),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id"),
            primary_key=True,
            nullable=False
        ),
)


class Place(BaseModel, Base):
    """ A place to stay """
    # TODO add or replace class attributes
    __tablename__ = "places"
    city_id = Column(
       String(60),
       ForeignKey("cities.id"),
       nullable=False
    )
    user_id = Column(
        String(60),
        ForeignKey("users.id"),
        nullable=False
    )
    name = Column(
        String(128),
        nullable=False
    )
    description = Column(
        String(1024),
        nullable=True
    )
    number_rooms = Column(
        Integer,
        nullable=False,
        default=0
    )
    number_bathrooms = Column(
        Integer,
        nullable=False,
        default=0
    )
    max_guest = Column(
        Integer,
        nullable=False,
        default=0
    )
    price_by_night = Column(
        Integer,
        nullable=False,
        default=0
    )
    latitude = Column(
        Float,
        nullable=True,
    )
    longitude = Column(
        Float,
        nullable=True,
    )
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") != 'db':
        from models.review import Review
        from models.amenity import Amenity

        @property
        def reviews(self):
            """ the : getter attribute reviews"""
            list_reviews = []
            for k, v in models.storage.all(Review).items():
                if self.id == Review.place_id:
                    list_reviews.append(v)
            return list_reviews

        @property
        def amenities(self):
            """ Getter attribute"""
            list_amenity = []
            for k, v in models.storage.all(Amenity).items():
                if amenity_id in self.amenity_ids:
                    list_amenity.append(v)
            return list_amenity

        @amenities.setter
        def amenities(self, obj=None):
            """Setter attribute"""
            if obj not in self.amenity_ids and isinstance(obj, Amenity):
                self.amenities.append(obj.id)

    reviews = relationship(
        "Review",
        backref="place",
        cascade="all, delete"
    )

    amenities = relationship(
        "Amenity",
        secondary="place_amenity",
        viewonly=False,
        backref="Place"
    )
