#!/usr/bin/python3
"""Deletes the State objects whose name contains the letter a.

Every matching state is removed from the database and the deletion is
committed.
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
    states = session.query(State).filter(State.name.like("%a%")).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
