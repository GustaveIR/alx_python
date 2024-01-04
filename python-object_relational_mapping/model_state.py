"""Start link class to table in database"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    try:
        engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}",
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        print("Table created successfully.")
    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
