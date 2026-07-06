from unittest.mock import patch, MagicMock
from main import app

def test_homepage():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

def test_homepage_content_type():
    client = app.test_client()

    response = client.get("/")

    assert "text/html" in response.content_type

@patch("main.client.chat.completions.create")
def test_ask_endpoint(mock_create):
    fake_response = MagicMock()
    fake_response.choices = [
    MagicMock(
        message=MagicMock(
            content="This is a mocked AI response."
        )
    )
    ]

    mock_create.return_value = fake_response

    client = app.test_client()

    response = client.post(
        "/ask",
        data={"question": "Hello"}
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["response"] == "This is a mocked AI response."


@patch("main.client.chat.completions.create")
def test_summarize_endpoint(mock_create):

    fake_response = MagicMock()
    fake_response.choices = [
        MagicMock(
            message=MagicMock(
                content="This is a mocked summary."
            )
        )
    ]

    mock_create.return_value = fake_response

    client = app.test_client()

    response = client.post(
        "/summarize",
        data={"email": "Hello, this is a long email."}
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["response"] == "This is a mocked summary."


def test_invalid_route():
    client = app.test_client()

    response = client.get("/this-route-does-not-exist")

    assert response.status_code == 404


@patch("main.client.chat.completions.create")
def test_empty_question_returns_400(mock_create):

    client = app.test_client()

    response = client.post(
        "/ask",
        data={}
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Question is required"

    mock_create.assert_not_called()

@patch("main.client.chat.completions.create")
def test_empty_email_returns_400(mock_create):

    client = app.test_client()

    response = client.post(
        "/summarize",
        data={}
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Email is required"

    mock_create.assert_not_called()