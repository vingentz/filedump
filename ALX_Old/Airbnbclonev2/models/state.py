#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import models
from models.base_model import Base
from models.city import City
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class  MySQL databse.

      Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get  list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
