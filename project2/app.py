from __future__ import absolute_import
import sentry_sdk
import logging
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

logger = logging.getLogger(__name__)

sentry_sdk.init(
    dsn="http://09a8352435f846a7b59fc73fe9c18c63@dev.getsentry.net:8000/9",

    environment="this environment",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/debug')
def trigger_error():
    try:
        1 / 0
    except Exception:
        logger.error("divided by zero?")
    return 'hi'


@app.route('/debug1')
def trigger_error1():
    trigger_inner_error()


def trigger_inner_error():
    1 / 0
