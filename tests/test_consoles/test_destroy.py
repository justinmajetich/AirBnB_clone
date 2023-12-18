from io import StringIO
import os
import unittest
from unittest import mock
import sys
import uuid

from console import HBNBCommand


class TestConsoleDestroy(unittest.TestCase):
    def setUp(self):
        mock_stdin = mock.create_autospec(sys.stdin)
        mock_stdout = mock.create_autospec(sys.stdout)

        self.hbnbCMD = HBNBCommand(stdin=mock_stdin, stdout=mock_stdout)

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_delete_no_class(self):
        with mock.patch("sys.stdout", new=StringIO()) as fake_out:
            self.hbnbCMD.onecmd("destroy")
            self.assertEqual("** class name missing **\n", fake_out.getvalue())

    def test_delete_no_uuid(self):
        with mock.patch("sys.stdout", new=StringIO()) as fake_out:
            self.hbnbCMD.onecmd("destroy User")
            self.assertEqual(
                "** instance id missing **\n",
                fake_out.getvalue(),
            )

    def test_delete_no_uuid_instance(self):
        with mock.patch("sys.stdout", new=StringIO()) as fake_out:
            self.hbnbCMD.onecmd("destroy User {}".format(uuid.uuid4()))
            self.assertEqual(
                "** no instance found **\n",
                fake_out.getvalue(),
            )

    def test_delete_new_object(self):
        with mock.patch("sys.stdout", new=StringIO()) as fake_out:
            self.hbnbCMD.onecmd("create User")
            id = fake_out.getvalue()
            fake_out.seek(0)
            fake_out.truncate(0)
            self.hbnbCMD.onecmd("destroy User {}".format(id.strip()))
            self.assertEqual(
                "",
                fake_out.getvalue(),
            )
