import requests

def test_question_001():
    text = "토큰이 중복 발급되었을 경우 어떻게 되나요?"
    response = requests.post(
        url='http://127.0.0.1:8000/chat',
        json={'sessionId': "tester_001", "text": text}
    )

    assert response.status_code == 200
