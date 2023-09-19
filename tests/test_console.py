import unittest
from console import HBNBCommand, do_create


class TestConsole(unittest.TestCase):
    def setUp(self):
        # Initialize any necessary objects or variables
        pass

    def tearDown(self):
        # Clean up any resources after each test
        pass

    def test_create_user(self):
        args = 'User email="example@example.com" password="mypassword" name="John Doe"'
        do_create(args)

        self.assertEqual(..., ...)

    def test_create_product(self):
        args = 'Product name="iPhone 13" price=1299.99 brand="Apple" description="Latest smartphone"'
        do_create(args)

    def test_create_car(self):
        args = 'Car make="Toyota" model="Camry" year=2022 mileage=5000'
        do_create(args)


if __name__ == '__main__':
    unittest.main()
