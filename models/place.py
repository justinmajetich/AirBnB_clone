#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, Float, Table
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
import models
from models.base_model import Base

if (models.storage_t == 'db'):
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    if (models.storage_t == 'db'):
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(128))
        number_rooms = Column(Integer(), default=0, nullable=False)
        number_bathrooms = Column(Integer(), default=0, nullable=False)
        max_guest = Column(Integer(), default=0, nullable=False)
        price_by_night = Column(Integer(), default=0, nullable=False)
        latitude = Column(Float())
        longitude = Column(Float())
        reviews = relationship("Review",  backref="place", cascade="delete")
        amenities = relationship("Amenity",  secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """Get a list of all reviews."""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

    def __init__(self, *args, **kwargs):
        """User class init
        """
        super().__init__(*args, **kwargs)
