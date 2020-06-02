from os import environ
from flask import Flask
from app.application import configure, blueprint
from common.app_logger import AppLogger

app = Flask(__name__)
configure("application.properties")
logger = AppLogger.instance().logger
logger.info("starting publication app ................!")
app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run()
