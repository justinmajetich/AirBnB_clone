#!/usr/bin/python3
"""
Define the ``Place`` class that inherits from the class ``BaseModel``
and the declarative base class 'Base'
"""

from models import storage
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.base_model import Base
from models.base_model import (
        Column,
        String,
        Integer,
        Float,
        relationship,
        ForeignKey,
        Table
        )

"""
An association table between the 'Place' and 'Amenity' models
"""
place_amenity = Table("place_amenity",
                      Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """
    Define the class Place

    * __tablename__: represents the table name, 'places'
    * city_id: represents a column containing a string (60 characters)
        * can't be null
        * is a foreign key to 'cities.id'
    * user_id (String): represents a column containing a string (60 characters)
        * can’t be null
        * is a foreign key to users.id
    * name (String): represents a column containing a string (128 characters)
        * can’t be null
    * description (String): represents a column containing a string \
(1024 characters)
        * can't be null
    * number_rooms (Integer): represents a column containing an integer
        * can’t be null
        * default value: 0
    * number_bathrooms (Integer): represents a column containing an integer
        * can’t be null
        * default value: 0
    * max_guest (Integer): represents a column containing an integer
        * can’t be null
        * default value: 0
    * price_by_night (Integer): represents a column containing an integer
        * can’t be null
        * default value: 0
    * latitude (Float): represents a column containing a float
        * can be null
    * longitude (Float): represents a column containing a float
        * can be null
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=(0))
    number_bathrooms = Column(Integer, nullable=False, default=(0))
    max_guest = Column(Integer, nullable=False, default=(0))
    price_by_night = Column(Integer, nullable=False, default=(0))
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = list(str())   # list of Amenity.id

    # Relationships:
    if isinstance(storage, DBStorage):
        # DBStorage relationship between 'Place' and other models
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 back_populates="place_amenities",
                                 viewonly=False)
    elif isinstance(storage, FileStorage):
        # FileStorage relationship between 'Place' and objects
        @property
        def reviews(self):
            """
            Return a list of 'Review' instances with place_id equal to
            self.id
            """
            objs = list()
            for obj in storage.all():
                if obj.place_id == self.id:
                    objs.append(obj)

            return objs

        @property
        def amenities(self):
            """
            Return a list of 'Amenity' instances linked to the Place object
            """
            from models.amenty import Amenity

            objs = list()
            for obj in storage.all(Amenity):
                if obj.place_id == self.id:
                    objs.append(obj)

            return objs

        @amenities.setter
        def amenities(self, obj):
            """
            Add the id of an Amenity object to self.amenity_ids

            NOTE: This method accepts only Amenity objects
            Otherwise do nothing
            """
            from models.amenity import Amenity

            if isinstance(obj, Amenity):
                sefl.amenity_ids.append(obj.id)
