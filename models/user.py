#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place

class User(BaseModel, Base):
    """This class defines a user by various attributes and stores user information"""

    __tablename__ = 'users'

   """This class defines a user by various attributes"""

    email = Column(String(128), nullable=False) 
    password = Column(String(128), nullable=False)
    first_name = Column(String(128)
    last_name = Column(String(128)

   """class attribute places must represent a relationship with the class Place"""

    if models.storage_type == 'db':
        places = relationship("Place", cascade="all, delete", back_populates="user")
    else:
        @property
        def places(self):
            from models import storage
            from models.place import Place
            all_places = storage.all(Place)
            return [place for place in all_places.values() if place.user_id == self.id]

    """
    from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review

class User(BaseModel, Base):
    """User class for storing user information"""

    __tablename__ = 'users'

    # ... other attributes ...

    if models.storage_type == 'db':
        reviews = relationship("Review", cascade="all, delete", back_populates="user")
    else:
        @property
        def reviews(self):
            from models import storage
            from models.review import Review
            all_reviews = storage.all(Review)
            return [review for review in all_reviews.values() if review.user_id == self.id]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

