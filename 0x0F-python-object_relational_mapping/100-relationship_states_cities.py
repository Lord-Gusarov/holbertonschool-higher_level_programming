#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
to the specified database passed as an argument.
"""
from sys import argv
from sqlalchemy import create_engine, orm
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import relationship


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = orm.sessionmaker(bind=engine)()

    cali_s = State(name='California')
    sanF_c = City(name='San Francisco', state=cali_s)
    session.add(cali_s, sanF_c)
    session.commit()

    session.close()
