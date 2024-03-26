from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state', cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        if 'cities' in kwargs:
            kwargs['cities'] = [City(**city) for city in kwargs.pop('cities')]
        super().__init__(*args, **kwargs)

    def __str__(self):
        return '[State] ({}) {}'.format(self.id, self.name)

    def to_dict(self):
        dic = super().to_dict()
        dic['cities'] = [city.to_dict() for city in dic.pop('cities', [])]
        return dic