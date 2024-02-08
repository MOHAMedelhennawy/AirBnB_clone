#!/usr/bin/python3
"""Unittest base.
Test cases for FileStorage class.
"""

import unittest
import os
from time import sleep
import datetime
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestStorage(unittest.TestCase):
    """Test class for FileStorage class."""

    def test_save(self):
        """Testing for the save method"""

        self.assertTrue(os.path.exists("file.json"))
        all_objs = storage.all()
  
        self.assertEqual(len(all_objs), 0)
        self.assertIsInstance(all_objs, dict)
        self.assertEqual(type(FileStorage()), FileStorage)
        # Check if file exist
        # Check if data is stored in file successfully

        with self.assertRaises(TypeError) as msg:
            all_objs = storage.all("This arg")
        excepted_output = "FileStorage.all() takes 1 positional argument but 2 were given"
        self.assertEqual(excepted_output, str(msg.exception))

        with self.assertRaises(TypeError) as msg:
            my_model = BaseModel()
            my_model.save("This arg")
        excepted_output = "BaseModel.save() takes 1 positional argument but 2 were given"
        self.assertEqual(excepted_output, str(msg.exception))

if __name__ == '__main__':
    unittest.main()