#!/usr/bin/python3

"""This module defines useful short methods that are heavily used during
testing."""

from io import StringIO
from uuid import UUID as uuid
from random import choice


class LazyMethods:
    """Defines useful short methods that are heavily used during testing."""

    __random_attributes = {
        "first_name": ["John", "Lucy", "Lisa", "Bob", "Betty"],
        "last_name": ["Doe", "Sickle", "Walters", "Range", "Holberton"],
        "age": [45, 98, 23, 40, 12, 67],
        "latitude": [
            37.773972,
            -89.2312,
            -14.5512,
            36.2148,
            45.1231,
            -66.2312,
            78.5512,
        ],
        "longitude": [
            -179.2312,
            -14.5512,
            36.2148,
            145.1231,
            -66.2312,
            78.5512,
        ],
    }

    @staticmethod
    def get_uuid(line: StringIO) -> uuid:
        """Returns the UUID from a string."""
        return uuid(line.getvalue().strip())

    @staticmethod
    def get_instances_count(line: StringIO) -> int:
        """Returns the integer value for the number of instances of a model."""
        return int(line.getvalue().strip())

    @staticmethod
    def get_key(model_name: str, instance_id: uuid) -> str:
        """Generates the key used in the objects dictionary for an instance."""
        return f"{model_name}.{instance_id}"

    def get_first_name(self) -> str:
        """Returns a first name."""
        return choice(self.__random_attributes["first_name"])

    def get_last_name(self) -> str:
        """Returns a first name."""
        return choice(self.__random_attributes["last_name"])

    def get_email(self, first_name: str = None, last_name: str = None) -> str:
        """Returns an email address based on random first and last names."""
        return (
            f"{first_name or self.get_first_name()}."
            f"{last_name or self.get_last_name()}@lzcorp.it".lower()
        )

    def get_random_attribute(self):
        """Generates a random key and a value corresponding to that key."""
        key = choice(list(self.__random_attributes.keys()))

        return key, choice(self.__random_attributes[key])
