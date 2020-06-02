import logging
from logging.handlers import RotatingFileHandler
from common.singleton import Singleton
import configparser

_LOGGING_FORMAT = 'logging.format'
_LOGGING_FILE_SUFFIX = 'logging.filesuffix'
_LOGGING_DIRECTORY = 'logging.directory'
_LOGGING_COUNT = 'logging.backup.count'
_LOGGING_BYTES = 'logging.maxsize.bytes'
_LOGGING_CONSOLE_LEVEL = 'logging.console.level'


@Singleton
class AppLogger:
    """
    This class will enable logger to the app
    need to create the class instance by using class.instance()
    and configure the logging
    """

    def __init__(self):
        self.logger = logging.getLogger()

    def configure(self, logging_properties_file):
        """
        This method will be responsible for configuring the logging
        for app
        :param logging_properties_file: file path of logging poperties
        """
        config = configparser.RawConfigParser()
        config.read(logging_properties_file)
        configs = dict(config.items('logging'))
        self.setup_logging(configs.get(_LOGGING_DIRECTORY), configs.get(_LOGGING_FILE_SUFFIX),
                           configs.get(
                               _LOGGING_FORMAT), int(configs.get(_LOGGING_BYTES)), int(configs.get(
                _LOGGING_COUNT)), configs.get(_LOGGING_CONSOLE_LEVEL))
        pass

    def setup_logging(self, dir_path, file_name, log_foramt, size, count, level):
        # Main logger
        self.logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        if level == 'info':
            console_handler.setLevel(logging.INFO)
        else:
            console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(logging.Formatter(log_foramt))

        file_handler = RotatingFileHandler('{}/{}_debug.log'.format(dir_path, file_name), maxBytes=size,
                                           backupCount=count)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(log_foramt))

        errors_file_handler = RotatingFileHandler('{}/{}_error.log'.format(dir_path, file_name), maxBytes=size,
                                                  backupCount=count)
        errors_file_handler.setLevel(logging.WARNING)
        errors_file_handler.setFormatter(logging.Formatter(log_foramt))

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(errors_file_handler)
