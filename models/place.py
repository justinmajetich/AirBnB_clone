#!/usr/bin/python3
"""Place Module for HBNB project."""
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from os import environ
from models.review import Review


class Place(BaseModel, Base):
    """A place to stay."""

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if environ.get("HBNB_ENV") == "db":
        reviews = relationship("Review", backref="place", cascade="delete")
    else:
        @property
        def reviews(self):
            """Review getter."""
            return [o for o in storage.all(Review) if o.place_id == self.id]

    def __init__(self, *args, **kwargs):
        """Init method."""
        filtered_kwargs = {
                k: v for k, v in kwargs.items()
                if hasattr(self, k) or k == "id"
                }
        super().__init__(*args, **filtered_kwargs)
