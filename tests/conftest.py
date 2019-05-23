import pytest

from hello.app import application


@pytest.fixture(scope='session')
def session_test_client():
    """
    Create a test version of the flask app to use for testing
    :return:
    """
    app = application.test_client()
    return app
