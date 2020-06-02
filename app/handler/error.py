from common.app_logger import AppLogger
from app.error.publication_errors import NotFoundError, ConfigKeyNotFoundError, InvalidConfigurationError
from app.handler.http import create_response
import traceback

logger = AppLogger.instance().logger


def create_error_response(exception):
    """
    This Method will be responsible for handling the errors
    in the service
    :param exception: expects the exception for handling
    :return: http response with exception message and corresponding status
    """
    logger.error(traceback.print_tb(exception.__traceback__))
    if isinstance(exception, NotFoundError):
        return create_response(getattr(exception, 'message', str(exception)), 404)
    elif isinstance(exception, ConfigKeyNotFoundError):
        return create_response(getattr(exception, 'message', str(exception)), 400)
    elif isinstance(exception, InvalidConfigurationError):
        return create_response(getattr(exception, 'message', str(exception)), 400)
    else:
        logger.error("error : {}".format(getattr(exception, 'message', str(exception))))
        return create_response("Internal server error", 500)
