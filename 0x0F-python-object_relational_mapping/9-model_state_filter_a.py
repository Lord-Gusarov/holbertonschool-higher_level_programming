#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the
specified database
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

    for record in session.query(State).order_by(State.id):
        if ('a' in record.name):
            print("{}: {}".format(record.id, record.name))

    session.close()
