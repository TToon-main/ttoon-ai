import boto3, sys, os
from configs import s3_config

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

def s3_connection():
    try:
        s3 = boto3.client(
            service_name = "s3",
            region_name = "ap-northeast-2", # 자신이 설정한 bucket region
            aws_access_key_id = s3_config.S3_KEY,
            aws_secret_access_key = s3_config.S3_SECRET_KEY,
        )
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!")
        return s3

# def s3_put_object(s3, bucket, filepath, access_key):
#     """
#     s3 bucket에 지정 파일 업로드
#     :param s3: 연결된 s3 객체(boto3 client)
#     :param bucket: 버킷명
#     :param filepath: 파일 위치
#     :param access_key: 저장 파일명
#     :return: 성공 시 True, 실패 시 False 반환
#     """
#     try:
#         s3.upload_file(
#             Filename=filepath,
#             Bucket=bucket,
#             Key=access_key,
#             ExtraArgs={"ContentType": "image/png", "ACL": "public-read"},
#         )
#     except Exception as e:
#         return False
#     return True

