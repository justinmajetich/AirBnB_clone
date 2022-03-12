#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from os import getenv
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


association_table = Table(
	'place_amenity',
	Base.metadata,
	Column('place_id', String(60), ForeignKey('places.id'), primary_key = True, nullable = False),
	Column('amenities_id', String(60), ForeignKey('amenities.id'), primary_key = True, nullable = False)
)


class Place(BaseModel, Base):
	""" A place to stay """
	__tablename__ = 'places'
	city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
	user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
	name = Column(String(128), nullable=False)
	description = Column(String(1024), nullable=False)
	number_rooms = Column(Integer, default=0, nullable=False)
	number_bathrooms = Column(Integer, default=0, nullable=False)
	max_guest = Column(Integer, default=0, nullable=False)
	price_by_night = Column(Integer, default=0, nullable=False)
	latitude = Column(Float, nullable=False)
	longitude = Column(Float, nullable=False)
	amenities = relationship('Amenity', secondary = association_table, viewonly=False, back_populates = 'places')
	reviews = relationship("Review", order_by = Review.id, back_populates = "place", cascade='all, delete')
	user = relationship("User", order_by = Place.id, back_populates = "place")
	cities = relationship("City", order_by = Place.id, back_populates = "place")
	amenity_ids = []

	if getenv('HBNB_TYPE_STORAGE', None) != 'db':
		@property
		def reviews(self):
			""" Get a list of all linked reviews """
			review_list = []
			for review in models.storage.all(Review).values():
				if review.place_id ==self.id:
					review_list.append(review)
			return review_list

		@property
		def amenities(self):
			""" Get linked amenities """
			amenity_list = []
			for amenity in model.storage.all(Amenity).values():
				if amenity.id in self.amenity_ids:
					amenity_list.append(amenity)
			return amenity_list

		@amenities.setter
		def amenities(self, value):
			if type(value) == Amenity:
				self.amenity_ids.append(value.id)
