#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
	""" State class """
	__tablename__ = 'states'
	name =  Column(String(128), nullable=False)
	if getenv('HBNB_TYPE_STORAGE') == 'db':
		cities = relationship("City",  backref="state", cascade="all, delete")
	else:	
		@property
		def cities(self)
			"""" Getter attribute to retrieve City object ""
			city_list = []
			for city in models.storage.all('City').values():
				if city.state_id == self.id:
					city_list.append(city)
			return city_list
