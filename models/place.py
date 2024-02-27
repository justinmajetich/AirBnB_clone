#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship

place_amenity = Table("place_amenity", Base.metadata,
                    Column('place_id', String(60), ForeignKey('places.id'),
                    primary_key=True, nullable=False),
                    Column('amenity_id', String(60), ForeignKey('amenities.id'),
                    primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="place")
        amenities = relationaship("Amenity", secondary=place_amenity, viewonly=False, back_populates="place_amenities")

    else:
        @property
        def reviews(self):
            """Return reviews.id list"""
            mod = models.storage.all()
            tmp = []
            final = []
            for key in var:
                check = key.replace('.', ' ')
                check = shlex.split(check)
                if (check[0] == 'Review'):
                    tmp.append(var[key])
            for elem in tmp:
                if (elem.plac_id == self.id):
                    final.append(elem)
            return (final)

        @property
        def amenities(self):
            """Return amenity_ids list"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """Append"""
            from models.amenity import Amenity
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)

