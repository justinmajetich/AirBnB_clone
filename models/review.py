

#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """This is the class for Review
    Inherits from SQLAlchemy Base and links to the MySQL table reviews.
    Attributes:
        place_id: (sqlalchemy String): The review's place id.
        user_id: (sqlalchemy String): The review's place id.)
        text: (sqlalchemy String): The review description
    """

    __tablename__ = "reviews"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ''
        user_id = ''
        text = ''
