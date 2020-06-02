import configparser
from enum import Enum
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from common.app_logger import AppLogger
from common.crypto import CryptoAES
from common.singleton import Singleton

_DATABASE_PASSWORD = 'database.password'
_DATABASE_USER = 'database.user'
_DATABASE_NAME = 'database.name'
_DATABASE_HOST = 'database.host'
_DATABASE_TYPE = 'database.type'
_DATABASE_POOL = 'database.pool'
_DATABASE_MAX_OVERFLOW = 'database.maxoverflow'
_DATABASE_SCHEMA = 'database.schema'
crypt = CryptoAES()


class DATABASE_TYPES(Enum):
    POSTGRES = 'postgres'
    ORACLE = 'oracle'
    MY_SQL = 'mysql'


@Singleton
class DataBase:
    """
    This class will be responsible for creating
    database connection pool object using sqlalchemy
    engine , need to create object class.instance()
    and configure database properties
    """

    def __init__(self):
        self.engine = None
        self.logger = AppLogger.instance().logger
        self.schema = 'datahub'
        pass

    def configure(self, properties):
        self.engine = self.create_base_engine(properties)

    def create_base_engine(self, properties):
        """
        This method will be responsible for creating
        database engine with connection pool
        :param properties: expects filepath of configuration propeties
        :return: engine
        """
        config = configparser.RawConfigParser()
        config.read(properties)
        configs = dict(config.items('database'))
        self.schema = str(configs[_DATABASE_SCHEMA])
        if configs[_DATABASE_TYPE] == DATABASE_TYPES.POSTGRES.value:
            return self.create_postgres_engine(configs)
        else:
            raise NotImplementedError("database flovour : {} not implemented".format(configs[_DATABASE_TYPE]))

    def get_session(self):
        """
        This method will be helpful in geeting the session
        from any point in the app
        :return: session object
        """
        self.Session = sessionmaker()
        self.Session.configure(bind=self.engine)
        self.logger.info("session opened")
        return self.Session()

    def get_schema(self):
        return self.schema

    def create_postgres_engine(self, configs):
        self.logger.info("initializing sqlachemy connectionpool .......")
        engine = create_engine(
            'postgresql://{0}:{1}@{2}/{3}'.format(configs[_DATABASE_USER], crypt.decrypt(configs[_DATABASE_PASSWORD]),
                                                  configs[_DATABASE_HOST], configs[_DATABASE_NAME]),
            pool_size=int(configs[_DATABASE_POOL]), max_overflow=int(configs[_DATABASE_MAX_OVERFLOW]))
        self.logger.info("sqlachemy engine created [ pool_size = {} ]".format(configs[_DATABASE_POOL]))
        return engine

    def close(self, session):
        session.close()
        self.logger.info("session closed")

    def close_all(self):
        self.logger.info("closing all sessions ....!")
        self.Session.close_all()
        self.logger.info("closed ....!")
