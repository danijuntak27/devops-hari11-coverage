from app.main import app

def test_home_route():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert b"Integration" in response.data

def test_ping_route():
    tester = app.test_client()
    response = tester.get("/ping")
    assert response.status_code == 200
    assert response.data == b"pong"
