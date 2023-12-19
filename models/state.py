#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import backref, relationship


# class State(BaseModel, Base):
#     """ State class """
#     __tablename__ = 'states'
#     name = Column(String(128), nullable=False)
#     cities = relationship('City', backref=backref('state'))

#     def cities_g(self):
#         """getter for cities relationship for FileStorage"""
#         print(BaseModel.all_classes(BaseModel, 'City'))
class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref=backref('state'))

    @staticmethod
    def cities_g(self):
        """getter for cities relationship for FileStorage"""
        City_Class = BaseModel.all_classes(BaseModel, 'City')
        result = models.storage.all(City_Class)
        # print(type(result))
        # print(result)
        selected_city = {k: v for k, v in result.items()
                         if v.state_id == self.id}
        #print(list(selected_city.values())[0], "//////////////////////")
        return selected_city
