#!/usr/bin/python3
"""Defines unittests - models/review.py.

 Presumpts existence of a `Review` class as defined in models/review.py
"""

import os
import unittest
from datetime import datetime
from time import sleep
#from models import storage
from models.review import Review
import models
from unittest.mock import patch
import random
import string


class TestReview_instantiation(unittest.TestCase):
  """Unittests - testing the Review class."""

  def test_invalid_id_type(self):
    """ builds Review with non-string ID ."""
    with self.assertRaises(TypeError):
      Review(id=123)

  def test_random_string_id(self):
    """ creates Review with a random string ID works."""
    id_length = 10
    random_id = ''.join(
        random.choices(string.ascii_letters + string.digits, k=id_length))
    rv = Review(id=random_id)
    self.assertEqual(random_id, rv.id)

  def test_kwargs_with_extra_keys(self):
    """creating a Review with extra kwargs doesn't cause errors."""
    dt = datetime.today()
    dt_iso = dt.isoformat()
    rv = Review(id="345",
                created_at=dt_iso,
                updated_at=dt_iso,
                extra_attr="value")
    self.assertEqual(rv.id, "345")
    self.assertEqual(rv.created_at, dt)
    self.assertEqual(rv.updated_at, dt)
    self.assertNotIn("extra_attr", rv.__dict__)

  class TestReview_save(unittest.TestCase):
    """Unittests - testing save method of the Review class."""

    @classmethod
    def setUpClass(cls):
      """Prepares clean testing file."""
      try:
        os.remove("file.json")
      except FileNotFoundError:
        pass

    def test_one_save(self):
      """save - updates the updated_at attribute and persists to storage."""
      rv = Review()
      sleep(0.05)
      first_updated_at = rv.updated_at
      rv.save()
      self.assertLess(first_updated_at, rv.updated_at)
      self.assertIn(rv.id, models.storage.all().keys())

    def test_two_saves(self):
      """ multiple saves update updated_at and persist correctly."""
      rv = Review()
      sleep(0.05)
      first_updated_at = rv.updated_at
      rv.save()
      second_updated_at = rv.updated_at
      self.assertLess(first_updated_at, second_updated_at)
      sleep(0.05)
      rv.save()
      self.assertLess(second_updated_at, rv.updated_at)
      self.assertIn(rv.id, models.storage.all().keys())

    def test_save_with_arg(self):
      """ saves raises TypeError when given argument."""
      rv = Review()
      with self.assertRaises(TypeError):
        rv.save(None)

    @patch('models.storage.save_object')
    def test_save_calls_storage_save(self, mock_save):
      """ saves calls the storage.save_object method."""
      rv = Review()
      rv.save()
      mock_save.assert_called_once_with(rv)

    def tearDownClass(cls):
      """Deletes temporary file after all tests."""
      try:
        os.remove("file.json")
      except FileNotFoundError:
        pass


class TestReview_save(unittest.TestCase):
  """Unittests - testing save method of Review class."""

  @classmethod
  def setUpClass(cls):
    """Prepares clean file for testing."""
    try:
      os.remove("file.json")
    except FileNotFoundError:
      pass

  def test_one_save(self):
    """ save updates the updated_at attribute and persists to storage."""
    rv = Review()
    sleep(0.05)
    first_updated_at = rv.updated_at
    rv.save()
    self.assertLess(first_updated_at, rv.updated_at)
    self.assertIn(rv.id, models.storage.all().keys())

  def test_two_saves(self):
    """multiple saves update updated_at and persist correctly."""
    rv = Review()
    sleep(0.05)
    first_updated_at = rv.updated_at
    rv.save()
    second_updated_at = rv.updated_at
    self.assertLess(first_updated_at, second_updated_at)
    sleep(0.05)
    rv.save()
    self.assertLess(second_updated_at, rv.updated_at)
    self.assertIn(rv.id, models.storage.all().keys())

  def test_save_with_arg(self):
    """ save raises a TypeError when given an argument."""
    rv = Review()
    with self.assertRaises(TypeError):
      rv.save(None)

  @patch('models.storage.save_object')
  def test_save_calls_storage_save(self, mock_save):
    """saves calls the storage.save_object method."""
    rv = Review()
    rv.save()
    mock_save.assert_called_once_with(rv)

  def tearDownClass(cls):
    """Deletes temporary file after tests."""
    try:
      os.remove("file.json")
    except FileNotFoundError:
      pass


if __name__ == "__main__":
  unittest.main()
