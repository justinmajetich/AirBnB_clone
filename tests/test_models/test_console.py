import unittest

from console import kwargs_create


class TestKwargsCreate(unittest.TestCase):

    def setUp(self):
        self.obj = kwargs_create(
        )  # Assuming the function is part of a class called YourClass

    def test_string_integer_float_args(self):
        args = ['key1=string', 'key2=123', 'key3=3.14']
        result = self.obj.kwargs_create(args)
        self.assertEqual(result, {'key1': 'string', 'key2': 123, 'key3': 3.14})

    def test_args_with_special_characters(self):
        args = ['name=John_Doe', 'age=25']
        result = self.obj.kwargs_create(args)
        self.assertEqual(result, {'name': 'John Doe', 'age': 25})

    def test_empty_args_list(self):
        args = []
        result = self.obj.kwargs_create(args)
        self.assertEqual(result, {})


if __name__ == '__main__':
    unittest.main()
