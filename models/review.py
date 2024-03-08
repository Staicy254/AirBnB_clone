#!/usr/bin/python3
"""
Review class for clone
"""
from models.base_model import BaseModel


class Review(BaseModel):
  """
    A Review class for the AirBnB clone project.
    """

  place_id = ""  # Public class attribute: empty string for Place.id
  user_id = ""  # Public class attribute: empty string for User.id
  text = ""  # Public class attribute: empty string for review text
