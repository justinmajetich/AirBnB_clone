#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from datetime import datetime
import uuid


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not kwargs.get("id"):
            self.id = str(uuid.uuid4())

        if not kwargs.get("created_at"):
            self.created_at = datetime.now()

        # if not kwargs.get("updated_at"):
        #    self.updated_at = datetime.now()

        if not kwargs.get("name"):
            self.name = ""

        if isinstance(self.created_at, str):
            self.created_at = datetime.strptime(
                self.created_at, "%Y-%m-%dT%H:%M:%S.%f")

        # if isinstance(self.updated_at, str):
            # self.updated_at = datetime.strptime(
            # self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """Returns a string representation of the instance"""
        cls_name = self.__class__.__name__
        return '[{}] ({}) {}'.format(
            cls_name, self.id, {
                k: v for k, v in self.__dict__.items() if k != 'updated_at'}
        )
