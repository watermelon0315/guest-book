# Guest Book Project

## 프로젝트 개요
- 자기소개 페이지와 간단한 방명록을 남기고 볼 수 있는 웹페이지

## 설치 및 실행 방법
1. 리포지토리 클론
   ```bash
   git clone https://github.com/watermelon/guest-book.git
   cd guest-book
2. 가상환경 설정 및 패키지 설치
   python3 -m venv myenv
   source myenv/bin/activate
   pip install -r requirements.txt
3. 서버 실행
   uvicorn main:app --host 0.0.0.0 --port 8000
   

API 엔드포인트

GET /: 자기소개 페이지
POST /guestbook: 방명록 작성
GET /guestbook: 방명록 목록 조회
DELETE /guestbook/{entry_id}: 방명록 항목 삭제

사용된 오픈 소스 라이브러리
FastAPI
Uvicorn

배포 링크
AWS에서 배포된 서비스 링크: http://100.28.146.73:8000/

학번 / 이름
학번: 2020508069
이름: 정소연
