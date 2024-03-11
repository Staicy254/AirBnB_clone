#!/usr/bin/python3
import uuid
from datetime import datetime
#from models import storage


class BaseModel:
  """
    A base class for other models.
    """

  def __init__(self, *args, **kwargs):
    """The __init__ sets up objects when they are created.

    self: Displays the instance of the class.
    *args and **kwargs: Allows passing variable numbers of arguments.
     """
    if kwargs is not None and kwargs != {}: #present object with attributes
      self.id = kwargs.get("id")
      if self.id is None:  # Assign ID if not already present
        self.id = str(uuid.uuid4())

      self.created_at = datetime.strptime(kwargs["created_at"],
                                          "%Y-%m-%dT%H:%M:%S.%f")
      self.updated_at = datetime.strptime(kwargs["updated_at"],
                                          "%Y-%m-%dT%H:%M:%S.%f")

      for key, value in kwargs.items():
        if key not in ["id", "created_at", "updated_at", "__class__"]:
          setattr(self, key, value)

    else:
      self.id = str(uuid.uuid4())
      self.created_at = self.updated_at = datetime.now()
    self.id = str(uuid.uuid4())  # Get unique ID as string
    self.created_at = datetime.utcnow()  # datetime at creation
    self.updated_at = self.created_at  # Updated time still same as creation

  def __str__(self):
    """
    String representation of the object.
    """
    return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

  def save(self):
    """
    Updates the updated_at attribute with the current datetime and potentially saves the object.
    """
    self.updated_at = datetime.now()

  def to_dict(self):
    """
    Retrieves a dictionary representation of the object.
    """
    my_dict = self.__dict__.copy()
    my_dict["__class__"] = self.__class__.__name__
    my_dict["created_at"] = self.created_at.isoformat()
    my_dict["updated_at"] = self.updated_at.isoformat()
    return my_dict
