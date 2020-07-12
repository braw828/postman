# SQL-Alchemy db_creator.py

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine(
'postgres://postgres:nevermind@localhost/int0', echo=True
)
Base = declarative_base()

class user_name(Base):
    __tablename__ = "more_users"
    id = Column(Integer, primary_key=True)
    user = Column(String, nullable=False)
    password = Column(String, nullable=False)
    def __init__(self,user,password):
        self.password = password
        self.user = user
class user_info(Base):
    __tablename__ = "user_info"
    id = Column(Integer, primary_key=True)
    user_Fname = Column(String, nullable=False)
    user_Lname = Column(String, nullable=False)
    user_age = Column(String, nullable=False)
    creat_date = Column(Date)
    user_id = Column(Integer, ForeignKey("more_users.id")) # gets id from more
    users = relationship("more_users",
                        backref=backref("user_info",
                        order_by=id
                                     ))
    def __init__(self,user_Fname,user_Lname,user_age,creat_date):
        self.user_Fname = user_Fname
        self.user_Lname = user_Lname
        self.user_age = user_age
        self.creat_date = creat_date

# Create tables

Base.metadata.create_all(engine)

