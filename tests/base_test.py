""" Base test class for all test classes. """
from pathlib import Path
from unittest import TestCase
import shutil
import os
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage

test_file = Path(__file__).parent / "tmp_file.json"


class BaseTest(TestCase):
    """Base class for all test classes."""

    @classmethod
    def setUpClass(cls):
        """
        keep copy of __objects, and clear it
        make test_file an empty file
        keep name of __filepath
        set __filepath to test_file
        """
        cls.original_storage = FileStorage._FileStorage__objects.copy()
        FileStorage._FileStorage__objects.clear()
        with open(test_file, 'w') as f:
            pass
        cls.orginal_file_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__file_path = test_file

    @classmethod
    def tearDownClass(cls):
        """
        copy back contents of __objects
        reset __file_path
        remove test_file
        """
        FileStorage._FileStorage__objects = cls.original_storage.copy()
        FileStorage._FileStorage__file_path = cls.orginal_file_path
        if test_file.exists():
            os.remove(test_file)

    def setUp(self):
        """
        set onecmd
        set objects
        """
        self.onecmd = HBNBCommand().onecmd
        self.objects = FileStorage._FileStorage__objects

    def teardown(self):
        """
        clear __objects
        clear test_file
        delete one cmd
        delete objects
        """
        FileStorage._FileStorage__objects.clear()
        with open(test_file, 'w') as f:
            pass
        del self.onecmd
        del self.objects

    def clear(self, stdout):
        """clear stdout StringIO object."""
        if not isinstance(stdout, StringIO):
            return
        stdout.seek(0)
        stdout.truncate(0)
