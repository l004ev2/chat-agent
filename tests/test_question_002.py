import requests

def test_question_002():
    text = "정보 전송 요구 연장은 언제 가능한가요?"
    response = requests.post(
        url='http://127.0.0.1:8000/chat',
        json={'sessionId': "tester_002", "text": text}
    )

    assert response.status_code == 200