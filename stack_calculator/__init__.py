import os
import flask

from stack_calculator.redisstore import RedisStore
from stack_calculator.handlers import api


def create_app(config):
    """Creates the Flask app instance."""
    flask_app = flask.Flask(__name__)
    flask_app.redis = RedisStore(config['redis_host'], config['redis_port'])
    flask_app.register_blueprint(api, url_prefix="/calc")
    return flask_app


config = { 'redis_host': 'localhost', 'redis_port': 16379}
app = create_app(config)
