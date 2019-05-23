import logging

import flask
from flask import Response
from flask.logging import default_handler
from hello import settings

application = flask.Flask(__name__)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

if settings.LOGGING_LEVEL == 'DEBUG':
    log_level = logging.DEBUG
elif settings.LOGGING_LEVEL == 'WARN':
    log_level = logging.WARN
elif settings.LOGGING_LEVEL == 'ERROR':
    log_level = logging.ERROR
elif settings.LOGGING_LEVEL == 'FATAL':
    log_level = logging.FATAL
else:
    log_level = logging.INFO

handler = default_handler
handler.setFormatter(formatter)
application.logger.removeHandler(default_handler)
application.logger.addHandler(handler)

application.logger.setLevel(log_level)


@application.route('/', methods=['GET'], strict_slashes=False)
def heartbeat():
    return Response(response='hello world!', status=200, mimetype="text/html")


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=settings.PORT)
