#!/usr/bin/python3
'''Test for console'''
import unittest
from console import HBNBCommand


class test_Console(unittest.TestCase):
    '''Define the test_console class'''

    def test_moduleDocs(self):
        '''
        Docs
        '''
        moduleDoc = __import__("console").__doc__
        self.assertGreater(len(moduleDoc), 0)


if __name__ == "__main__":
    unittest.main()
