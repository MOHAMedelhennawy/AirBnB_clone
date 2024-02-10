#!/usr/bin/python3
"""Unittest base.
Test cases for FileStorage class.
"""

import unittest
import os
from time import sleep
import datetime
import json
import models
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test class for FileStorage class."""

    def setUp(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_FileStorage(self):
        """
        Test FileStorage attributes
        """
        self.assertIsInstance(FileStorage(), FileStorage)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertIsInstance(storage, FileStorage)
        with self.assertRaises(TypeError) as Err_msg:
            obj_Test = FileStorage("This arg")

    def test_deleted_file(self):
        """
        Test that file deleted successfully
        """

        self.assertFalse(os.path.exists("file.json"))

    def test_attributes(self):
        """
        Test FileStorage class attribute
        """
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertEqual(FileStorage._FileStorage__objects, {})
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all(self):
        """
        Test all method
        """
        all_objs = storage.all()
        self.assertEqual(all_objs, {})
        self.assertIsInstance(all_objs, dict)
        self.assertFalse(os.path.exists("file.json"))
        with self.assertRaises(TypeError) as msg:
            all_objs = storage.all("This arg")
        Err_msg = (
            "all() takes 1 positional argument but 2 were given"
                   )
        self.assertEqual(Err_msg, str(msg.exception))

    def test_save(self):
        """
        Test save method
        """

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertTrue(os.path.exists("file.json"))
        all_objs = storage.all()
        self.assertNotEqual(all_objs, {})
        self.assertEqual(len(all_objs), 1)
        self.assertNotEqual(len(all_objs), 0)
        with self.assertRaises(TypeError) as msg:
            my_model.save("This arg")
        Err_msg = (
            "save() takes 1 positional argument but 2 were given"
                   )
        self.assertEqual(Err_msg, str(msg.exception))

    def test_new(self):
        """
        Test new method
        """
        my_model = BaseModel()
        self.assertTrue(bool(FileStorage._FileStorage__objects))

    def test_reload(self):
        """
        Test reload method
        """
        my_model = BaseModel()
        my_model.save()
        storage = FileStorage()
        all_objs = storage.all()
        obj = all_objs['BaseModel.{}'.format(my_model.id)]
        self.assertEqual(obj, my_model)
        with self.assertRaises(TypeError) as msg:
            storage.reload("This arg")
        Err_msg = (
            "reload() takes 1 positional argument but 2 were given"
                   )
        self.assertEqual(Err_msg, str(msg.exception))


if __name__ == '__main__':
    unittest.main()
