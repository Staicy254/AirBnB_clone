#!/usr/bin/python3
"""Module that carries file storage class"""

import json
from datetime import datetime 

class FileStorage:
  """Serializes instances to a JSON file and deserializes JSON file to instances."""

  __file_path = "file.json"  # Default file path
  __objects = {}  # Dictionary that stores objects

  def __init__(self, file_path=None):
    """Begins the FileStorage instance.

    Args:
      file_path (str, optional): The path to the JSON file. Defaults to "file.json".
    """
    if file_path:
      self.__file_path = file_path
    self.reload()

  def all(self):
    """Outputs a dictionary of all stored objects."""
    return self.__objects

  def new(self, obj):
    """Puts a new object to the storage."""
    key = f"{obj.__class__.__name__}.{obj.id}"
    self.__objects[key] = obj

  def save(self):
    """Serializes all objects to the JSON file."""
    try:
      # Includes timestamps in serialized data
      objdict = {key: value.to_dict() for key, value in self.__objects.items()}
      for obj in objdict.values():
        obj['updated_at'] = datetime.utcnow().isoformat()
      with open(self.__file_path, "w") as f:
        json.dump(objdict, f)
    except Exception as e:
      print(f"Error saving to file: {e}")

  def reload(self):
    """Deserializes the JSON file to objects."""
    try:
      with open(self.__file_path, "r") as f:
        objdict = json.load(f)
        for key, value in objdict.items():
          self.new(eval(value["_class_"]))
    except FileNotFoundError:
      pass  # No action if the file doesn't exist
