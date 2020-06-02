from flask import make_response
from app.error.publication_errors import ConfigKeyNotFoundError


def create_response(data, status_code):
    """
    This method will be responsible for creating
    response object for request
    :param data: expects output of requested operation
    :param status_code: expects http status code
    :return: http response with message and status
    """
    response = make_response(data, status_code)
    response.headers.set('Content-Security-Policy', "default-src 'self'")
    return response


def get_pagination_variables(request):
    '''
    This method will be helpful for extracting
    pagination values from http request object
    :param request: expects http request object
    :return: offset value and size  if valid else throws badrequest exception
    '''
    try:
        page = int(request.args.get('page'))
        size = int(request.args.get('size'))
    except Exception as e:
        raise ConfigKeyNotFoundError(
            "Bad Request (page:int,size:int) query params expected as example:(http(s)://<url>?page=1&size=10) ")

    offset = 0 if page <= 1 else (page - 1) * size
    return (offset, size)
