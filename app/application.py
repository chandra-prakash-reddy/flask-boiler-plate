import multiprocessing

from flask import Blueprint
from flask_restplus import Api


from common.app_logger import AppLogger
from common.database import DataBase
from app.controller.app import api as app_ns

blueprint = Blueprint('api', __name__)
api = Api(blueprint,
          title='Sample Application',
          version='1.0',
          description='rest api for demo'
          )

# add all names_spaces here
api.add_namespace(app_ns, path='/api')


def configure(props):
    AppLogger.instance().configure(props)
    DataBase.instance().configure(props)


def cleanup():
    DataBase.instance().close_all()

# atexit.register(cleanup)
