#!/usr/bin/python3
"""Prints the id of the State object whose name is given as argument.

The name searched is passed to the query as a parameter, so no SQL
injection is possible, and ``Not found`` is printed when no state
matches it.
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
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)
    session.close()
