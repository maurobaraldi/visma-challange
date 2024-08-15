import pytest

from json import loads
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        return client


def test_health_check(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert loads(res.get_data(as_text=True)) == {"status": "ok"}

@pytest.mark.skip(reason="This test must be mocked to run on github actions.")
def test_download(app, client):
    del app
    res = client.get('/1')
    assert res.status_code == 200
    assert res.content_type in ('image/png', "application/pdf")