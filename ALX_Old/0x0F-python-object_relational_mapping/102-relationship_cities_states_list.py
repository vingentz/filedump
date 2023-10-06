#!/usr/bin/python3
"""Script listing all City objects from database"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    stacit = session.query(State).outerjoin(City).order_by(City.id).all()

    for state in stacit:
        for city in state.cities:
            print('{}: {} -> {}'.format(city.id, city.name, state.name))
