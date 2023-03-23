#!/usr/bin/python3
'''Test for the ``console.py`` module'''

from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestConsole(TestCase):
    '''Testcase for console functionality'''

    def setUp(self) -> None:
        self.con = HBNBCommand()

    def test_quit_works(self):
        '''tests that ``quit`` command quits correctly'''
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd('quit')

    def test_EOF_works(self):
        '''tests that ``EOF`` shortcut works'''
        with self.assertRaises(SystemExit):
                HBNBCommand().onecmd('EOF')
            


class TestCreate(TestCase):
    '''Testcase for the ``create`` command'''

    def test_create_fails_without_modelname(self):
        '''checks that create without a model name fails'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create')
            self.assertEqual(f.getvalue().strip(), '** class name missing **')

    def test_create_works_with_no_attrs(self):
        '''checks that create can be called without attributes'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State')
            self.assertTrue(len(f.getvalue().strip()) == 36)

    def test_create_works_with_attributes(self):
        '''checks that ``create`` command works with attrs'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Arizona"')
            self.assertTrue(len(f.getvalue().strip()) == 36)

    def test_attrs_are_set_correctly(self):
        '''checks that attrs are properly set on created instance'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Arizona"')
            uid = f.getvalue().strip()
            test_dict = storage.all()[f"State.{uid}"].__dict__
            self.assertEqual(test_dict['name'], 'Arizona')

    def test_attrs_are_properly_casted(self):
        '''checks that attrs are casted correctly'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Arizona" num_of_rooms=34 lattitude=34.3456')
            uid = f.getvalue().strip()
            test_dict = storage.all()[f"State.{uid}"].__dict__
            self.assertTrue(type(test_dict['name']), str)
            self.assertTrue(type(test_dict['num_of_rooms']), int)
            self.assertTrue(type(test_dict['lattitude']), float)