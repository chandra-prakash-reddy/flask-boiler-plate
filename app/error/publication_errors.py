"""
    This Exception will be helping in raising the errors
    where items are not available for request
"""


class NotFoundError(Exception):
    pass


"""
    This Exception will be helping in raising the errors
    where request is made with Invalid data
"""


class ConfigKeyNotFoundError(Exception):
    pass


"""
    This Error will be raised
    where items are requested with Invalid configuration provided
"""


class InvalidConfigurationError(Exception):
    pass
