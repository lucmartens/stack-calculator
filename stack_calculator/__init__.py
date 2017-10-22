import flask
from redis import StrictRedis

from stack_calculator.handlers import api


def create_app(config):
    """Create Flask app instance."""
    flask_app = flask.Flask(__name__)
    flask_app.redis = StrictRedis(host=config['redis_host'],
                                  port=config['redis_port'],
                                  db=config['redis_db'])
    flask_app.register_blueprint(api, url_prefix="/calc")
    return flask_app


config = {'redis_host': 'localhost', 'redis_port': 16379, 'redis_db': 0}
app = create_app(config)
