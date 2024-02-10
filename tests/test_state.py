#!/usr/bin/python3
"""Unittest User.
Test cases for User class.
"""


import unittest
import json
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import os

class TestBase(unittest.TestCase):
    """
    Test class for State class
    """

    def setUp(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_state(self):
        """
        Test if file.json created successfully
        """

        state_obj = State()
        self.assertFalse(os.path.exists("file.json"))
        state_obj.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_attributes(self):
        """
        Test state class attribute
        """
        state_obj = State()
        state_obj.name = "Betty"
        self.assertEqual(state_obj.name, "Betty")
        self.assertIsInstance(state_obj, State)
        self.assertIsInstance(state_obj.name, str)
        self.assertIsNotNone(state_obj.id)
        self.assertIsInstance(state_obj.id, str)
        state_obj2 = State(name="My_First_Name", my_number=43)
        self.assertEqual(state_obj2.name, "My_First_Name")
        self.assertIsInstance(state_obj2.name, str)
        self.assertEqual(state_obj2.my_number, 43)
        self.assertIsInstance(state_obj2.my_number, int)
