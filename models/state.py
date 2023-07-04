#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship

if os.getenv("HBNB_TYPE_STORAGE") == 'DB':
    
class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    
    cities =relationship("City", backref="state", cascade="all", delete")

else:

    class State(BaseModel):
    """ File storage State """
    name = ""
    
    @property
    def cities(self):
        """ Returns list of City instances with state id = to the current State id"""
        
        list_cities = []
        for key, city in storage.all(City).items():
            if city.state_id == self.id:
                list_cities.append(city)
            return list_cities