#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)