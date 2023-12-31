#!/usr/bin/python3
"""
Defines unittests for console.py
"""

from io import StringIO
from unittest import mock, TestCase, main
from console import HBNBCommand


class TestHBNBCommand_create(TestCase):
    """Defines unittests for tests create

    Args:
        TestCase (_type_): _description_
    """
    def setUp(self) -> None:
        self.sys_out = mock.patch('sys.stdout', new=StringIO(), spec=True)
        self.patcher = self.sys_out.start()
        
    def test_class_name_missing(self):
        self.assertFalse(HBNBCommand().onecmd("create"))
        self.assertEqual('** class name missing **',
                         self.patcher.getvalue().strip())
    
    def test_class_does_not_exist(self):
        self.assertFalse(HBNBCommand().onecmd('create MyUser'))
        self.assertEqual("** class doesn't exist **",
                         self.patcher.getvalue().strip())
    
    def tearDown(self) -> None:
        self.sys_out.stop()
    
if __name__ == '__main__':
    main()