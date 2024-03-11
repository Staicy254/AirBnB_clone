#!/usr/bin/python3
"""Defines unittests for models/city.py."""

import os
import unittest
from datetime import datetime
from time import sleep

from models import storage  
from models.city import City  


class TestCity_instantiation(unittest.TestCase):
  """ testing init of  City class."""

  def test_no_args_instantiates(self):
      """ city class builds an example."""
      self.assertEqual(City, type(City()))

  def test_new_instance_stored_in_objects(self):
      """  new City example is stored in storage.all().values()."""
      city = City()  # Create an instance explicitly
      self.assertIn(city, storage.all().values())

  def test_id_is_public_str(self):
      """city class.id is of type str."""
      self.assertEqual(str, type(City().id))

  def test_created_at_is_public_datetime(self):
      """ City class.created_at is of type datetime."""
      self.assertEqual(datetime, type(City().created_at))

  def test_updated_at_is_public_datetime(self):
      """ City class.updated_at is of type datetime."""
      self.assertEqual(datetime, type(City().updated_at))

  def test_state_id_is_public_class_attribute(self):
      """  City.state_id is a public class attribute (not instance-level)."""
      cy = City()
      self.assertEqual(str, type(City.state_id))
      self.assertIn("state_id", dir(cy))
      self.assertNotIn("state_id", cy.__dict__)

  def test_name_is_public_class_attribute(self):
      """City.name is a public class attribute (not instance-level)."""
      cy = City()
      self.assertEqual(str, type(City.name))
      self.assertIn("name", dir(cy))
      self.assertNotIn("name", cy.__dict__)

  def test_two_cities_unique_ids(self):
      """check two City instances have unique IDs."""
      cy1 = City()
      cy2 = City()
      self.assertNotEqual(cy1.id, cy2.id)

  def test_two_cities_different_created_at(self):
      """check two City instances have different created_at timestamps."""
      cy1 = City()
      sleep(0.05)
      cy2 = City()
      self.assertLess(cy1.created_at, cy2.created_at)

  def test_two_cities_different_updated_at(self):
      """check two City instances have different updated_at timestamps."""
      cy1 = City()
      sleep(0.05)
      cy2 = City()
      self.assertLess(cy1.updated_at, cy2.updated_at)

  def test_str_representation(self):
      """string representation of a City instance."""
      dt = datetime.today()
      dt_repr = repr(dt)
      cy = City()
      cy.id = "123456"
      cy.created_at = cy.updated_at = dt
      cystr = cy.__str__()
      self.assertIn("[City] (123456)", cystr)
      self.assertIn("'id': '123456'", cystr)
      self.assertIn("'created_at': " + dt_repr, cystr)
      self.assertIn("'updated_at': " + dt_repr, cystr)

  def test_args_unused(self):
      """checks if arguments passed to City() are not used."""
      cy = City(None)
      self.assertNotIn(None, cy.__dict__.values())

  def test_instantiation_with_kwargs(self):
      """ init using keyword arguments for id, created_at, and updated_at."""
      dt = datetime.today()
      dt_iso = dt.isoformat()
      cy = City(id="345", created_at=dt_iso, updated_at=dt_iso)
      self.assertEqual(cy.id, "345")
    self.assertEqual(cy.created_at, dt)
            self.assertEqual(cy.updated_at, dt)

        def test_instantiation_with_None_kwargs(self):
            """ passing None for keyword arguments raises TypeError."""
            with self.assertRaises(TypeError):
                City(id=None, created_at=None, updated_at=None)


    class TestCity_save(unittest.TestCase):
        """Unittests - tests save method of City class."""

        @classmethod
        def setUp(self):
            """
            Renames existing "file.json" to "tmp" avoids conflicts during tests.
            """
            try:
                os.rename("file.json", "tmp")
            except OSError:
                pass

        def tearDown(self):
            """
            Starts removing "file.json" and then rename "tmp" back to "file.json"
            if exists, ensures cleanup after.
            """
            try:
                os.remove("file.json")
            except OSError:
                pass
            try:
                os.rename("tmp", "file.json")
            except OSError:
                pass

        def test_one_save(self):
            """ save class updates updated_at and stores City instance."""
            cy = City()
            sleep(0.05)
            first_updated_at = cy.updated_at
            cy.save()
            self.assertLess(first_updated_at, cy.updated_at)
            self.assertIn(cy, storage.all().values())  

        def test_two_saves(self):
            """check multiple saves update updated_at correctly and persist changes."""
            cy = City()
            sleep(0.05)
            first_updated_at = cy.updated_at
            cy.save()
            second_updated_at = cy.updated_at
            self.assertLess(first_updated_at, second_updated_at)
            sleep(0.05)
            cy.save()
            third_updated_at = cy.updated_at
            self.assertLess(second_updated_at, third_updated_at)
            self.assertIn(cy, storage.all().values())  

        def test_save_with_arg(self):
            """check class raises TypeError when passed - argument."""
            cy = City()
            with self.assertRaises(TypeError):
                cy.save(None)

        def test_save_updates_file(self):
            """check class writes the City instance to storage file."""
            cy = City()
            cy.save()
            cyid = "City." + cy.id
            with open("file.json", "r") as f:
                self.assertIn(cyid, f.read())


    class TestCity_to_dict(unittest.TestCase):
        """tests to_dict method of City class."""

        def test_to_dict_type(self):
            """City class.to_dict() returns  dictionary."""
            self.assertTrue(dict, type(City().to_dict()))

        def test_to_dict_contains_correct_keys(self):
            """Checks if to_dict class includes essential keys (id, created_at, updated_at, __class__)"""
            cy = City()
            self.assertIn("id", cy.to_dict())
            self.assertIn("created_at", cy.to_dict())
            self.assertIn("updated_at", cy.to_dict())
            self.assertIn("__class__", cy.to_dict())

        def test_to_dict_contains_added_attributes(self):
            """Checks if to_dict class includes additional instance ."""
            cy = City()
            cy.middle_name = "Holberton"
            cy.my_number = 98
            self.assertEqual("Holberton", cy.middle_name)
            self.assertIn("my_number", cy.to_dict())

        def test_to_dict_datetime_attributes_are_strs(self):
            """Check if to_dict class converts datetime strings."""
            cy = City()
            cy_dict = cy.to_dict()
            self.assertEqual(str, type(cy_dict["id"]))
            self.assertEqual(str, type(cy_dict["
            self.assertEqual(str, type(cy_dict["created_at"]))
                  self.assertEqual(str, type(cy_dict["updated_at"]))

        
        def test_to_dict_output(self):
                                     
                dt = datetime.today()
                cy = City()
                cy.id = "123456"
                cy.created_at = cy.updated_at = dt
                tdict = {
                    'id': '123456',
                    '__class__': 'City',
                    'created_at': dt.isoformat(),
                    'updated_at': dt.isoformat(),
                }
                self.assertDictEqual(cy.to_dict(), tdict)

              def test_contrast_to_dict_dunder_dict(self):
                """checks if to_dict class is different from the private __dict__ attribute."""
                cy = City()
                self.assertNotEqual(cy.to_dict(), cy.__dict__)

              def test_to_dict_with_arg(self):
                """checks if to_dict class raises TypeError when passed an argument."""
                cy = City()
                with self.assertRaises(TypeError):
                    cy.to_dict(None)


              if __name__ == "__main__":
              unittest.main()
