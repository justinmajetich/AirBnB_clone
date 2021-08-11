#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

# instance SQLAlchemy Table for relation Many-To-Many(Place-Amenity)
# https://docs.sqlalchemy.org/en/14/core/metadata.html
table_relation = Table('place_amenity',
                       Base.metadata,
                       Column('place_id',
                              String(60),
                              ForeignKey('places.id'),
                              primary_key=True,
                              nullable=False),
                       Column('amenity_id',
                              String(60),
                              ForeignKey('amenities.id'),
                              primary_key=True,
                              nullable=False))


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
    # check if the origin of the data is from db
    origin_data = os.getenv("HBNB_TYPE_STORAGE")
    # if come from db_storage
    if (origin_data == "db"):
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
        amenities = relationship("Amenity", secondary=place_amenity,
                                 backref="place", viewonly=False)
    # if come from file_storage
    else:
        @property
        def reviews(self):
            """Getter reviews"""
            reviews = models.storage.all(City)
            list_reviews = []
            for idx in reviews.values():
                if self.id == idx.state_id:
                    list_reviews.append(idx)
            return list_reviews

        @property
        def amenities(self):
            """Getter for amenities with FileStorage engine"""
            amenities = models.sotrage.all(Amenity)
            list_amenity = []
            for idx in amenities.values():
                if self.id == idx.amenity_ids:
                    list_amenity.append(idx)
            return list_amenity

        @amenities.setter
        def amenities(self, value):
            """ Setter for amenities method"""
            if type(value) is Amenity:
                amenities.append(value)
