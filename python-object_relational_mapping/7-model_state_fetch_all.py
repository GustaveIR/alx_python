#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def fetch_all_states(username, password, database):
    """Fetch all State objects from the database and display them."""
    # Create an engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and display all states
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    fetch_all_states(username, password, database)
