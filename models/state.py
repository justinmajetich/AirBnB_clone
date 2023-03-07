from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City

class State(BaseModel, Base):
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            from models import storage
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
