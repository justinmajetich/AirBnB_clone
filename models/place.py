#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128))
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False))

    if os.getenv("HBNB_TYPE_STROAGE") == 'db':
        reviews = relationship('Review', cascade='all, delete',
                               backref='place')
        amenities = relationship("Amenity", secondary=place_amenity,
                                 backref='place_amenity', viewonly=False)
    else:

        @property
        def reviews(self):
            '''returns the list of Review instances with
               place_id equals to the current Place.id'''
            ret = []
            # get dictionary of all out objects
            all_objs_dict = storage.all()
            # loop through our dict for key, value
            for key, value in all_objs_dict.items():
                # if we're at a Review object
                if key.split('.')[0] == 'Review' and self.id == value.place_id:
                    # append it
                    ret.append(value)
            return ret

        @property
        def amenities(self):
            ''' amenities '''

            adict = storage.all(Amenity)
            alist = []
            for v in adict.values():
                if Amenity.id in self.amenity_ids:
                    alist.append(value)
            return alist

        @amenities.setter
        def amenities(self, value=None):
            ''' amenity setter '''
            from models.amenity import Amenity

            if value:
                if type(value).__name__ == 'Amenity':
                    self.amenity_ids.append(value.id)
