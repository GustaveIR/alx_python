#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}",
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Displaying records
    states = session.query(State).all()
    print("Existing records:")
    for state in states:
        print(f"ID: {state.id}, Name: {state.name}")

    # Inserting records
    new_state = State(name="New State")
    session.add(new_state)
    session.commit()
    print("New record added.")

    # Displaying records after insertion
    states = session.query(State).all()
    print("Records after insertion:")
    for state in states:
        print(f"ID: {state.id}, Name: {state.name}")

if __name__ == "__main__":
    main()
