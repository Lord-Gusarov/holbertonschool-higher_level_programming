#!/usr/bin/python3
"""
That prints all City objects from the database passed as an argument
The script takes 3 arguments: mysql username, mysql password and database name
"""
from sys import argv
from sqlalchemy import create_engine, orm
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = orm.sessionmaker(bind=engine)()

    records = (session
               .query(State.name, City.id, City.name)
               .filter(City.state_id == State.id)
               .order_by(City.id))
    for rec in records:
        print("{}: ({}) {}".format(*rec))

    session.close()
