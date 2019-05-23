import pytest


@pytest.mark.root
class TestContentRoot(object):
    def test_root_return_200(self, session_test_client):
        response = session_test_client.get('/', headers={
        })
        assert 200 == response.status_code
        assert b'hello world!' == response.data
