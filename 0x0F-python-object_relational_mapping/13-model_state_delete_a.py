#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' from the
database passed as an argument
"""
from sys import argv
import sqlalchemy
from sqlalchemy import create_engine, orm
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = orm.sessionmaker(bind=engine)()

    for state in session.query(State).all():
        if ('a' in state.name):
            session.delete(state)

    session.commit()
    session.close()
