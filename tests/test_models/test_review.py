#!/usr/bin/python3
"""Defines unittests for Review class."""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class TestReview(test_basemodel):
    """Unittests for Review class."""

    def __init__(self, *args, **kwargs):
        """Initialize instance."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review