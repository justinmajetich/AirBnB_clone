#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Table, Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from models import storage_type

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if storage_type == 'db':
        reviews = relationship('Review',
                               backref='place',
                               cascade="all, delete")
        amenities = relationship('Amenity',
                                 secondary=place_amenity,
                                 viewonly=False,
                                 back_populates='place_amenities')
    else:
        @property
        def amenities(self):
            from models import storage
            result = [amenity for amenity in storage.all(Amenity).values()
                      if amenity.id in self.amenity_ids]
            return result

        @amenities.setter
        def amenities(self, obj):
            '''Setter attribute that handles append method
            for adding an Amenity.id to the attribute amenity_ids
            '''
            if obj.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)

        @property
        def reviews(self):
            ''' returns the list of Review instances with place_id
            equals to the current Place.id
            '''
            from models import storage
            result = [review for review in storage.all(Review).values()
                      if review.place_id == self.id]
            return result
