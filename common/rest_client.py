import requests
from common.app_logger import AppLogger

_GET = 'GET'
_POST = 'POST'


class RestFulClient:
    """
    This method will be helpful in executing the http requests
    """

    def __init__(self):
        self.app_logger = AppLogger.instance().logger
        pass

    def delete(self, url, headers={}):
        """
        This method responsible to perform http delete operation
        :param url: expects http(s)://<url>
        :param headers: expects http headers
        :return: http response object
        """
        try:
            self.app_logger.debug('request : {}'.format(url))
            response = requests.delete(url, headers=headers)
            if (response.status_code == 200):
                self.app_logger.debug("request successful")
                return response
            else:
                self.app_logger.debug(
                    "request unsucessful  code {0} :  {1}".format(response.status_code, response.text))
                response = {}
        except Exception as e:
            self.app_logger.error(e)
        finally:
            return response

    def get(self, url, headers={}):
        """
          This method responsible to perform http get operation
          :param url: expects http(s)://<url>
          :param headers: expects http headers
          :return: http response object
          """
        try:
            self.app_logger.debug('request : {}'.format(url))
            response = requests.request(_GET, url, headers=headers)
            if (response.status_code == 200):
                self.app_logger.debug("request successful")
                return response
            else:
                self.app_logger.debug(
                    "request unsucessful code {0} :  {1}".format(response.status_code, response.text))
        except Exception as e:
            self.app_logger.error(e)
        finally:
            return response

    def post(self, url, headers={}, payload='{}'):
        """
        This method responsible to perform http get operation
        :param url: expects http(s)://<url>
        :param headers: expects http headers
        :param payload: expects input data for http request
        :return: http response object
        """
        try:
            self.app_logger.debug('request : {0} headers {1} '.format(url, headers))
            response = requests.request(_POST, url, data=payload, headers=headers)

            if (response.status_code in [200, 201]):
                self.app_logger.debug("request successful")
                return response
            else:
                self.app_logger.debug(
                    "request unsucessful  code {0} :  {1}".format(response.status_code, response.text))
                response = {}
        except Exception as e:
            self.app_logger.error(e)
        finally:
            return response
