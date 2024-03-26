from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class BaseModel:
    __tablename__ = ''
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            if k in ['created_at', 'updated_at']:
                continue
            if k not in self.__dict__:
                setattr(self, k, v)

    def __str__(self):
        cls = self.__class__.__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        from models import storage
        storage.new(self)
        storage.save()

    def delete(self):
        from models import storage
        storage.delete(self)
        storage.save()

    def to_dict(self):
        dic = {}
        for k, v in self.__dict__.items():
            if k[0] == '_' or k == 'storage':
                continue
            dic[k] = v
        return dic