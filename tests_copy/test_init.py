#!/usr/bin/python3
'''Unittest for the console __init__'''

import unittest
import models


class Test_Init(unittest.TestCase):
    '''Test models'''
    def test_module_docstring(self):
        '''Test documentation for the module'''
        self.assertTrue(len(models.__doc__))
