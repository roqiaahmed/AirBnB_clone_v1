#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models import storage_type, storage

if storage_type == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    if storage_type == "db":
        id = Column(String(60), unique=True, primary_key=True, nullable=False)
        created_at = Column(datetime, nullable=False, default=datetime.utcnow())
        updated_at = Column(datetime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            del kwargs["__class__"]
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split(".")[-1]).split("'")[0]
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""

        dictionary = self.__dict__.copy()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        dictionary[__class__] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        storage.delete(self)
