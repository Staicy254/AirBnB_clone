#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import os
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing BaseModel class."""

    # Tests - instantiation and basic attributes
    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    # Tests - uniqueness of attributes
    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    # Tests - string representation
    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    # Tests - save method
    def test_save_updates_updated_at(self):
        bm = BaseModel()
        first_updated_at = bm.updated_at
        bm.save()
        self.assertGreater(bm.updated_at, first_updated_at)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    # Tests - to_dict method (consider adding more as needed)
    # ... (place your additional to_dict tests here)
class TestBaseModel_to_dict(unittest.TestCase):
  """Unittests for testing to_dict method - BaseModel."""

  def test_to_dict_returns_dict(self):
      bm = BaseModel()
      self.assertTrue(dict, type(bm.to_dict()))

  def test_to_dict_contains_correct_keys(self):
      bm = BaseModel()
      bm_dict = bm.to_dict()
      self.assertIn("id", bm_dict)
      self.assertIn("created_at", bm_dict)
      self.assertIn("updated_at", bm_dict)
      self.assertEqual(str, type(bm_dict["id"]))
      self.assertEqual(str, type(bm_dict["created_at"]))
      self.assertEqual(str, type(bm_dict["updated_at"]))

  def test_to_dict_contains_added_attributes(self):
      bm = BaseModel()
      bm.name = "Holberton"
      bm.my_number = 98
      self.assertIn("name", bm.to_dict())
      self.assertIn("my_number", bm.to_dict())

  def test_to_dict_datetime_attributes_are_strs(self):
      bm = BaseModel()
      bm_dict = bm.to_dict()
      self.assertEqual(str, type(bm_dict["created_at"]))
      self.assertEqual(str, type(bm_dict["updated_at"]))

  def test_to_dict_output(self):
      dt = datetime.today()
      bm = BaseModel()
      bm.id = "123456"
      bm.created_at = bm.updated_at = dt
      tdict = {
          'id': '123456',
          '__class__': 'BaseModel',
          'created_at': dt.isoformat(),
          'updated_at': dt.isoformat()
      }
      self.assertDictEqual(bm.to_dict(), tdict)

  def test_contrast_to_dict_dunder_dict(self):
      bm = BaseModel()
      self.assertNotEqual(bm.to_dict(), bm.__dict__)

  def test_to_dict_with_arg(self):
      bm = BaseModel()
      with self.assertRaises(TypeError):
          bm.to_dict(None)


if __name__ == "__main__":
  unittest.main()
