#!/usr/bin/python3
"""Lists all the City objects of a database with their state.

The cities and the states are fetched together and printed sorted by
the id of the city.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    rows = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()
    for city, state in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
