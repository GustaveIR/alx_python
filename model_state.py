from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

# Replace 'mysql+mysqldb://username:password@localhost:3306/db_name' with your MySQL connection string
engine = create_engine('mysql+mysqldb://root:Strongerthanbefore1@@localhost:3306/db_name', echo=True)

# Create the table
Base.metadata.create_all(engine)

# Create a Session
Session = sessionmaker(bind=engine)
session = Session()
