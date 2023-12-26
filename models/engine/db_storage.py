#!/usr/bin/python3
"""

"""
# handles the details of how to connect to the database and execute SQL commands
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.exc import InvalidRequestError
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')


class DBStorage:
    """database storage for mysql conversion
    """
    __engine = None
    __session = None

    def __init__(self):
        """initializer for DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER,
            HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB), pool_pre_ping=True)
        env = getenv("HBNB_ENV")
        if (env == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        obj_dict = {}

        if cls:
            if isinstance(cls, str):
                cls = globals().get(cls)

                if cls and issubclass(cls, Base):
                    objs_list = self.__session.query(cls).all()
                    obj_dict = {"{}.{}".format(obj.__class__.__name__, obj.id): obj for obj in objs_list}
                else:
                    for subclass in Base.__subclasses__():
                        objs_list = self.__session.query(subclass).all()
                        obj_dict.update({"{}.{}".format(obj.__class__.__name__, obj.id): obj for obj in objs_list})

                return obj_dict
    
    def new(self, obj):
        """
        
        """
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """"
        
        """
        self.__session.commit()    

                
    def delete(self, obj=None):
        """
        
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create database session
        """
        # create session from current engine
        Base.metadata.create_all(self.__engine)
        # create db tables
        session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        # previousy:
        # Session = scoped_session(session)
        self.__session = scoped_session(session)

    def close(self):
        """Close scoped session
        """
        self.__session.close()
