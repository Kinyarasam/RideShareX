#!/usr/bin/env python3
"""
Contains the class DBStorage
"""
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.user import User
from models.ride import Ride
from models.ride_request import RideRequest
from dotenv import load_dotenv


load_dotenv()  # Load the enviroment variables
classes = {"User": User, "Ride": Ride,
           "RideRequest": RideRequest}


class DBStorage:
    """
    Interacts with the mySQL database
    """
    _session = None
    _engine = None

    def __init__(self):
        """
        Instantiates a DBStorage object
        """
        RIDESHAREX_MYSQL_USER = getenv("RIDESHAREX_MYSQL_USER")
        RIDESHAREX_MYSQL_PWD = getenv("RIDESHAREX_MYSQL_PWD")
        RIDESHAREX_MYSQL_HOST = getenv("RIDESHAREX_MYSQL_HOST")
        RIDESHAREX_MYSQL_DB = getenv("RIDESHAREX_MYSQL_DB")
        RIDESHAREX_ENV = getenv("RIDESHAREX_ENV")
        
        self._engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                     .format(
                                         RIDESHAREX_MYSQL_USER,
                                         RIDESHAREX_MYSQL_PWD,
                                         RIDESHAREX_MYSQL_HOST,
                                         RIDESHAREX_MYSQL_DB
                                     ))
        
        # if RIDESHAREX_ENV == "test":
        #     Base.metadata.drop_all(self._engine)

    def all(self, cls=None):
        """
        Query on the current database session
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self._session.query(classes[clss]).all()
                for obj in objs:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    new_dict[key] = obj
        return new_dict
    
    def new(self, obj):
        """
        Add the object to the current database session
        """
        self._session.add(obj)

    def save(self):
        """
        Commit all the changes of the current database session
        """
        self._session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session obj if not None
        """
        if obj is not None:
            self._session.delete(obj)

    def reload(self):
        """
        Reloads data from the database
        """
        Base.metadata.create_all(self._engine)
        sess_factory = sessionmaker(bind=self._engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self._session = Session

    def close(self):
        """
        Call remove() method on the private session attribute
        """
        self._session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and it's ID, or
        None if not found
        """
        if cls not in classes.values():
            return None
        
        all_cls = self.all(cls)
        for value in all_cls.values():
            if value.id == id:
                return value
        return None
    
    def find(self, cls, *args, **kwargs):
        """
        Returns a record matching parameters
        """
        if cls not in classes.values():
            return None
        
        return self._session.query(cls).filter_by(**kwargs).first()

    def count(self, cls=None):
        """
        Count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(self.all(clas).values())
        else:
            count = len(self.all(cls).values())

        return count
