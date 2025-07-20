import boto3

AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
S3_BUCKET_NAME = "lab-s3-webhosting-13459"
FILE_NAME = "20250717_16h42m33s.csv"

# AWS access
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name="ap-northeast-2"
)

try:
    # upload file
    s3_client.upload_file(f"./csv/{FILE_NAME}", S3_BUCKET_NAME, FILE_NAME)
    print(f"File successfully uploaded. file name : '{FILE_NAME}'")

except Exception as e:
    print(f"error occured : {e}")