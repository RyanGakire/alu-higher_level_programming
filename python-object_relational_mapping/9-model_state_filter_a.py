#!/usr/bin/python3
"""Lists the State objects whose name contains the letter a.

The filtering is done by the database, and the states are printed
sorted by id.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    states = session.query(State).filter(
        State.name.like("%a%")).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
