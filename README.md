## 1. 사전 준비 사항
- openai의 api 키를 발급받은 후 환경변수에 `OPENAI_API_KEY`라는 값으로 저장이 되어있어야 합니다.
```bash
export OPENAI_API_KEY="..."
```

## 2. 실행 환경
```bash
python3.12
```

## 3. 실행 방법
### 3.1 패키지 설치
```bash
pip install -r requirements.txt
pip install -e .
```
### 3.2 실행
```bash
python3 run_server.py
```
### 3.3. 테스트 페이지 접속 및 테스트
- http://0.0.0.0:8000/docs 접속
- `/chat` api 호출
