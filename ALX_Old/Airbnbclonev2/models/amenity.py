#!/usr/bin/python3
""" defines the class amenity """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """ A MySQL database representing an Amenity class.

     Inherits from SQLAlchemy Base and links to the MySQL table amenities.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
