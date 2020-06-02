from common.app_logger import AppLogger
from common.database import DataBase
from common.singleton import Singleton
import traceback


@Singleton
class DataBaseHelper:
    """
    This class will be responsible for performing
    the all database requests
    """

    def __init__(self):
        self.database = DataBase.instance()
        self.logger = AppLogger.instance().logger
        pass

    def get_schema(self):
        return self.database.get_schema()

    def convert_rows_to_dict_list(self, rows):
        """
        This method will be helpful in converting
        raw data database output to list of dictionaries
        :param rows: expect raw out of selected rows returned by session/engine/connection object
        :return: list of dictionaries
        """
        data = []
        info = rows.keys()
        for row in rows:
            line = {}
            for i, col in enumerate(row):
                line[info[i]] = col
            data.append(line)
        if len(data) == 1:
            return data[0]
        return data

    def execute_select_query(self, query, params):
        """
        This method will be responsible for executing
        select queries against the database
        :param query: expects query to be executed
        :param params: parameters for query if any
        :return: output results of query execution
        """
        try:
            self.logger.info("executing query : {} params :{}".format(query, params))
            session = self.database.get_session()
            return self.convert_rows_to_dict_list(session.execute(query, params))
        except Exception as e:
            self.logger.error(traceback.print_tb(e.__traceback__))
            raise e
        finally:
            self.database.close(session)

    def execute_update_query(self, query, params):
        """
        This method is responsible for executing
        DML queries against the database
        :param query: expects query to be executed
        :param params: parameters for query if any
        :return True if query executed successfully,
                False if query execution failed
        """
        try:
            self.logger.debug("executing query : {} params :{}".format(query, params))
            session = self.database.get_session()
            session.execute(query, params)
            session.commit()
        except Exception as e:
            self.logger.error(traceback.print_tb(e.__traceback__))
            raise e
        finally:
            self.database.close(session)
