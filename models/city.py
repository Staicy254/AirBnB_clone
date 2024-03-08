#!/usr/bin/python3
"""
City class performs inheritance from BaseModel 
"""
from models.base_model import BaseModel

class City(BaseModel):
  """
    City class for the AirBnB clone.
    """

  state_id = ""  # Public class attribute: empty string for State.id
  name = ""
