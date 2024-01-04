#!/usr/bin/python3
"""Start link class to table in database"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    __mapper_args__ = {
        'version_id_col': name,
        'version_id_generator': lambda v: datetime.now()
    }

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}", pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Display existing records
    existing_states = session.query(State).all()
    print("Existing records:")
    for state in existing_states:
        print(f"ID: {state.id}, Name: {state.name}")

    # Insert a new record
    new_state = State(name="New State")
    session.add(new_state)
    session.commit()
    print("New record added.")

    # Display records after insertion
    updated_states = session.query(State).all()
    print("Records after insertion:")
    for state in updated_states:
        print(f"ID: {state.id}, Name: {state.name}")

if __name__ == "__main__":
    main()

