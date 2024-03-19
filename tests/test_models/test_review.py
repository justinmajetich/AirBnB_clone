#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """ """

    data = {
        "Review.01d5b8b0-2f20-460a-a303-069a14fc7461": {
            "__class__": "Review",
            "created_at": "2024-03-19T09:19:30.585105",
            "id": "01d5b8b0-2f20-460a-a303-069a14fc7461",
            "place_id": "ed72aa02-3286-4891-acbc-9d9fc80a1103",
            "text": "Amazing place, huge kitchen",
            "updated_at": "2024-03-19T09:19:30.585359",
            "user_id": "d93638d9-8233-4124-8f4e-17786592908b",
        }
    }

    def setUp(self) -> None:
        self.review = Review(
            **self.data["Review.01d5b8b0-2f20-460a-a303-069a14fc7461"]
        )

    def test_place_id(self):
        """ """
        self.assertEqual(type(self.review.place_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.review.user_id), str)

    def test_text(self):
        """ """
        self.assertEqual(type(self.review.text), str)
