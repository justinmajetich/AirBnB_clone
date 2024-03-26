from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False)
    state = relationship('State', back_populates='cities')

    def __init__(self, *args, **kwargs):
        if 'state' in kwargs:
            kwargs['state_id'] = kwargs.pop('state')
        super().__init__(*args, **kwargs)

    def __str__(self):
        return '[City] ({}) {}'.format(self.id, self.name)

    def to_dict(self):
        dic = super().to_dict()
        dic['state_id'] = dic.pop('state_id')
        dic['state'] = dic.pop('state')
        return dic