#!/usr/bin/python3
"""
Write a script that lists all City objects from the database passed as an
argument but using the 'state' relationship.
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
    cities = session.query(City)
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
