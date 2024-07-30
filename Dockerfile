FROM python:3.10.9

# 작업 디렉토리 생성
WORKDIR /TTOON-AI

# 현재 디렉토리의 모든 파일을 컨테이너의 작업 디렉토리로 복사
COPY . .

# 필요한 패키지 설치 (requirements.txt 파일이 있다는 가정)
RUN pip install --no-cache-dir -r requirements.txt

# 컨테이너가 실행할 명령을 설정
CMD ["python", "app/app.py"]
