#!/usr/bin/python3
"""
Write a script that lists all State objects, and corresponding City objects,
contained in the database pased as an argument using the cities relationship
for all State objects.
* The Script takes 3 arguments: mysql username, mysql password and
  database name.
"""
from sys import argv
from sqlalchemy import create_engine, orm
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = orm.sessionmaker(bind=engine)()
    states = session.query(State)
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
