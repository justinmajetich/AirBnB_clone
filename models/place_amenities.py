#!/usr/bin/python3

"""Module containing place_amenities shared table"""
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.base_model import Base


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True),
                      extend_existing=True)
