from sqlalchemy import create_engine, ForeignKey, Column, String, CHAR, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    social_security_number = Column("social_security_number", Integer, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, social_security_number, first_name, last_name, gender, age):
        self.social_security_number = social_security_number
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.social_security_number}) {self.first_name} {self.last_name} ({self.gender} {self.age})"


# this is like the connector?
# it can accept lots of different ways of connection
# we could use an in memory database, maybe this is an interesting choice, how do we do it?
# can I leave just empty without including a name in the database?
engine = create_engine("sqlite:///mydb.db", echo=True)
# what does echo=True does?


# This line will take all the classes that extend from Base and create the equivalent table
Base.metadata.create_all(bind=engine)

# Stopped here:
# https://youtu.be/AKQ3XEDI9Mw?t=528
