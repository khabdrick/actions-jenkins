from main import app


def test_main():
    # Creates a test client for this application.
    response = app.test_client().get("/")
    # assert the status code of the page('/') is 200
    assert response.status_code == 200
    # assert the return statement ton the page
    assert response.data == b"Welcome to my Flask App"
