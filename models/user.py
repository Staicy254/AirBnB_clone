#!/usr/bin/python3
"""
User class for AirBnB clone
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class for the AirBnB clone.
    """

  email = ""  # Public class attribute: empty string
  password = ""  # Public class attribute: empty string (should be hashed before storing)
  first_name = ""  # Public class attribute: empty string
  last_name = ""  # Public class attribute: empty string
