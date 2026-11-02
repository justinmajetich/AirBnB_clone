#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, ForeignKey, Column, Integer, String, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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
    reviews = relationship('Review', cascade='delete', backref='place')

    place_amenity = Table(
        'place_amenity', Base.metadata, Column(
            'place_id', ForeignKey('places.id'), primary_key=True), Column(
            'amenity_id', ForeignKey('amenities.id'), primary_key=True))

    # if getenv("HBNB_TYPE_STORAGE") == 'db':
    amenities = relationship(
        'Amenity',
        secondary=place_amenity,
        viewonly=False)

    @property
    def cities(self):
        '''returns the list of Review instances with place_id
            equals the current Place.id
            FileStorage relationship between Place and Review
        '''
        from models import storage
        related_reviews = []

        reviews = storage.all(Review).items()
        for review in reviews.values():
            if review.place_id == self.id:
                related_reviews.append(review)
        return related_reviews
