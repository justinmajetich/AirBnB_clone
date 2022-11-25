#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref='place', cascade="all, delete")
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)

    @property
    def reviews(self):
        """Getter attribute reviews that returns the list of Review instances
        with place_id equals to the current Place.id
        """
        from models import storage
        my_list = []
        extracted_reviews = storage.all('Review').values()
        for review in extracted_reviews:
            if self.id == review.place_id:
                my_list.append(review)
        return my_list

    @property
    def amenities(self):
        """Getter attribute that returns the list of Amenity instances based on
        the attribute amenity_ids that contains all Amenity.id linked to the
        Place.
        """
        from models import storage
        my_list = []
        extracted_amenities = storage.all('Amenity').values()
        for amenity in extracted_amenities:
            if self.id == amenity.amenity_ids:
                my_list.append(amenity)
        return my_list

    @amenities.setter
    def amenities(self, obj):
        """Setter attribute that handles append method for adding an Amenity.id
        to the attribute amenity_ids.
        """
        if isinstance(obj, 'Amenity'):
            self.amenity_id.append(obj.id)
