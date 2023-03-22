#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__  = "place"

    city_id: Mapped[str] = mapped_column(String(60), ForeignKey("city.id"), nullable=False)
    user_id: Mapped[str] = mapped_column(String(60), ForeignKey("user.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    description = Mapped[str] = mapped_column(String(1024), nullable=False)
    number_rooms = Mapped[int] = mapped_column(nullable=False)
    number_bathrooms = Mapped[int] = mapped_column(nullable=False)
    max_guest = Mapped[int] = mapped_column(nullable=False)
    price_by_night = Mapped[int] = mapped_column(nullable=False)
    latitude = Mapped[float] = mapped_column(nullable=False)
    longitude = Mapped[float] = mapped_column(nullable=False)
    amenity_ids = []
