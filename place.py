#!/usr/bin/python3
""" Place Module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table
from models import storage_type
from models.amenity import Amenity
from models.review import Review


""" Defines the place_amenity table for the database storage case """
if storage_type == 'db':
    place_amenity = Table('Place_amenity', Base.metadata, Column(
        'place_id', String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
        ),
        Column(
            'amenity_id', String(60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False)
        )


class Place(BaseModel, Base):
    """ Place class defines a place by various attributes """
    __tablename__ = 'places'
    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        """Update to the backref name"""
        amenities = relationship(
                'Amenity', secondary=place_amenity,
                viewonly=False, backref='place_amenities')
        reviews = relationship(
                "Review", backref='place', cascade="all, delete, delete-orphan"
            )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

        @property
        def reviews(self):
            """Returns list of review instances with place_id"""
            from models import storage
            all_revs = storage.all(Review)
            lst = []
            for rev in all_revs.values():
                if rev.place_id == self.id:
                    lst.append(rev)
            return lst

        @property
        def amenities(self):
            """ Returns list of Amenity instances linked to a Place """
            from models import storage
            all_amens = storage.all(Amenity)
            lst = []
            for amen in all_amens.values():
                if amen.id in self.amenity_ids:
                    lst.append(amen)
            return lst

        @amenities.setter
        def amenities(self, obj):
            """Adding an Amenity.id to the attribute amenity_ids"""
            if obj is not None:
                if isinstance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)

