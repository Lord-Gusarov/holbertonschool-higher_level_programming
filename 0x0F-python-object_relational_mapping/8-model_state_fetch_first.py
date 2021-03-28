#!/usr/bin/python3
"""Prints the first State object from the database specified
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

    first = session.query(State).order_by(State.id).first()
    out = '' if first is None else '{}: {}'.format(first.id, first.name)
    print(out)

    session.close()
