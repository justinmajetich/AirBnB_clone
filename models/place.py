#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey
                             ('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"),
                     nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary='place_amenity',
                             viewonly=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def reviews(self):
            """ reviews getter for FileStorage

            Returns the list of Review instances with
            place_id equals to the current Place.id

            """
            from models import storage

            our_plcs = storage.all(Review)
            review_plcs = []
            for rev in our_plcs.values():
                if self.id == rev.id:
                    review_plcs.append(rev)

            return review_plcs

        @property
        def amenities(self):
            """
            getter amenity that returns the list of Amenity
            instances based on the attribute amenity_ids
            """
            from models import storage
            from models.amenity import Amenity

            our_amenities = storage.all(Amenity)
            plc_amenities = []
            for ame in our_amenities.values():
                if ame.id in self.amenity_ids:
                    plc_amenities.append(ame)
            return plc_amenities

        @amenities.setter
        def amenities(sef, obj=None):
            """
            Setter amenities, that handles append method for
            adding an Amenity.id to the attribute amenity_ids.
            """

            if type(obj) == 'Amenity':
                self.amenities_ids.append(obj.id)
