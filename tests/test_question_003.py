import requests

def test_question_003():
    text = "x-api-tran-id에 대해 알려주세요."
    response = requests.post(
        url='http://127.0.0.1:8000/chat',
        json={'sessionId': "tester_003", "text": text}
    )

    assert response.status_code == 200