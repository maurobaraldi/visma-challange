from json import loads


def test_health_check(app, client):
    del app
    res = client.get('/health')
    assert res.status_code == 200
    assert loads(res.get_data(as_text=True)) == {"status": "ok"}

def test_download(app, client):
    del app
    res = client.get('/1')
    assert res.status_code == 200
    assert res.content_type in ('image/png', "application/pdf")