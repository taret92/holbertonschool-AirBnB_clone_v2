#!/usr/bin/python3
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

"""class DBStorage"""

classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }


class DBStorage:
    """declarate class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """___init method"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        if cls is None:
            return {}
        else:
            filtered_dict = {}
            for k in self.__session.query(classes[cls.__name__]).all():
                if cls.__name__ == k.__class__.__name__:
                    filtered_dict[k.__class__.__name__ + "." + k.id] = k
            return filtered_dict

    def new(self, obj):
        """add an obj into db"""
        self.__session.add(obj)

    def save(self):
        """save the changes at db"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an obj from db"""
        self.__session.delete(obj)

    def reload(self):
        """reloads the data in the db"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
