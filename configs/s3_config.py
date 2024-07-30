from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일 로드

S3_KEY = os.getenv("S3_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")