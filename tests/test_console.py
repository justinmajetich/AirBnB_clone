#!/usr/bin/python3
""" """
from console import HBNBCommand
import unittest


class test_console(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'HBNBCommand'
        self.value = HBNBCommand

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        """ """
        pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_emptyline(self):
        """ """
        i = self.value()
        self.assertEqual(i.emptyline(), None)

    def test_do_quit(self):
        """ """
        i = self.value()
        with self.assertRaises(SystemExit):
            i.do_quit(None)

    def test_do_EOF(self):
        """ """
        i = self.value()
        with self.assertRaises(SystemExit):
            i.do_EOF(None)

    def test_do_create(self):
        """ """
        i = self.value()
        with self.assertRaises(TypeError):
            i.do_create()

    def test_do_show(self):
        """ """
        i = self.value()
        with self.assertRaises(TypeError):
            i.do_show()

    def test_do_destroy(self):
        """ """
        i = self.value()
        with self.assertRaises(TypeError):
            i.do_destroy()

    def test_do_all(self):
        """ """
        i = self.value()
        with self.assertRaises(TypeError):
            i.do_all()

    def test_do_update(self):
        """ """
        i = self.value()
        with self.assertRaises(TypeError):
            i.do_update()

    def test_do_count(self):
        """ """
        i = self.value()
        with self.assertRaises(TypeError):
            i.do_count()

    def test_do_create(self):
        """ """
        i = self.value()
        with self.assertRaises(TypeError):
            i.do_create()

    def test_do_show(self):
        """ """
        i = self.value()
        with self.assertRaises(TypeError):
            i.do_show()

    def test_do_all(self):
        """ """
        i = self.value()
        with self.assertRaises(TypeError):
            i.do_all()

    def test_do_update(self):
        """ """
        i = self.value()
        with self.assertRaises(TypeError):
            i.do_update()

    def test_do_count(self):
        """ """
        i = self.value()
        with self.assertRaises(TypeError):
            i.do_count()
