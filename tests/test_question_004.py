import requests

def test_question_004():
    text = "API 스펙 중 aNS는 어떤 것을 뜻하나요?"
    response = requests.post(
        url='http://127.0.0.1:8000/chat',
        json={'sessionId': "tester_004", "text": text}
    )

    assert response.status_code == 200