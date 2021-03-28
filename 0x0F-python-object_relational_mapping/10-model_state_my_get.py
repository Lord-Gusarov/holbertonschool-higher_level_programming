#!/usr/bin/python3
"""
Prints the id of the State objectwith the name passed as argument
from the database passed as argument.
"""
from sys import argv
import sqlalchemy
from sqlalchemy import create_engine, orm
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:4]), pool_pre_ping=True)
    toMatch = argv[4]
    Base.metadata.create_all(engine)
    session = orm.sessionmaker(bind=engine)()

    found = False
    for state in session.query(State):
        if (state.name == toMatch):
            print(state.id)
            found = True
            break
    if not found:
        print('Not found')

    session.close()
