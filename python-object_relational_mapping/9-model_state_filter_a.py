#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def filter_states_with_a(username, password, database):
    """Filter and display all State objects containing the letter 'a' from the database."""
    # Create an engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and display states containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.ilike('%a%')).order_by(State.id).all()
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    filter_states_with_a(username, password, database)
