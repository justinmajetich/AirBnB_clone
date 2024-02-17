from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if models.storage_t == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            cities_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
