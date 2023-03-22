#!/usr/bin/python3
""" Review module for the HBNB project """
from typing import Optional
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__  = "review"

    place_id: Mapped[str] = mapped_column(String(60), ForeignKey("place.id"), nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"), nullable=False)
    text: Mapped[Optional[str]]
