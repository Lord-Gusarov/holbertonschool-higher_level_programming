#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database passed as an argument
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

    lousiana = State(name="Louisiana")
    session.add(lousiana)
    session.commit()
    print(lousiana.id)

    session.close()
