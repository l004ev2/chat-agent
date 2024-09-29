import difflib
import requests

def test_multiturn():
    text1 = "토큰이 중복 발급되었을 경우 어떻게 되나요?"
    text2 = "다시 말해줘"
    user1_response_1 = requests.post(
        url='http://127.0.0.1:8000/chat',
        json={'sessionId': "tester_multi_1", "text": text1}
    )

    user1_response_2 = requests.post(
        url='http://127.0.0.1:8000/chat',
        json={'sessionId': "tester_multi_1", "text": text2}
    )

    user2_response_1 = requests.post(
        url='http://127.0.0.1:8000/chat',
        json={'sessionId': "tester_multi_1", "text": text2}
    )

    sm1 = difflib.SequenceMatcher(None, user1_response_1.json()["answer"], user1_response_2.json()["answer"])
    sm2 = difflib.SequenceMatcher(None, user1_response_1.json()["answer"], user2_response_1.json()["answer"])

    assert sm1.ratio() > 0.67
    assert sm2.ratio() < 0.67
