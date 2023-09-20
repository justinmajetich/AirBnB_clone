#!/usr/bin/python3
"""This script defines the Review class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """
        This is the review model.
        Inherits:
            BasemMdel
            Base
        Attributes:
            __tablename__: The name of the MySQL table for storing reviews.
        text: review description.
        place_id: id place, relatinship place
        user_id: id user, relationship user
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

