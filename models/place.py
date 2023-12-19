#!/usr/bin/python3
"""Place Module for HBNB project."""
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from os import getenv
from sqlalchemy.orm import relationship
# from models.amenity import Amenity
from models.base_model import BaseModel, Base


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"), nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id"),
           nullable=False)
    )

from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            "Review", backref="place", cascade="all, delete-orphan")
        # amenities = relationship("Amenity", secondary="place_amenity",
        # backref="place_amenities", viewonly=False)
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """
            getter attribute reviews that returns the list of Review
            instances with place_id equals to the current Place.id
            """
            from models import storage, classes

            reviews_list = (
                storage.all(classes['Review'])
                .values()
                )
            return [review for review in reviews_list if
                    review.place_id == self.id]

        @property
        def amenities(self):
            """
            Getter attribute amenities that returns the list of Amenity
            instances based on the attribute amenity_ids that contains
            all Amenity.id linked to the Place
            """
            from models import storage, classes
            amenity_list = storage.all(classes['Amenity']).values()
            return [amenity for amenity in amenity_list
                    if amenity.place_id == self.id]

        @amenities.setter
        def amenities(self, amenity_obj):
            """
            Setter attribute amenities that handles append method for
            adding an Amenity.id to the attribute amenity_ids. This method
            should accept only Amenity object, otherwise, do nothing.
            """
            from models import storage, classes
            if isinstance(amenity_obj, classes['Amenity']):
                self.amenity_ids.append(amenity_obj.id)
