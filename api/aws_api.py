from dotenv import load_dotenv, dotenv_values
import boto3
import os

env=".env" # 執行環境
load_dotenv(override=True)



class Aws_s3_api():
    def __init__(self):
        self.aws_client = boto3.client(
            's3',
            aws_access_key_id=dotenv_values(env)["access_key"],
            aws_secret_access_key=dotenv_values(env)["secret_access_key"],
        )
        self.bucket="yin-storage"
    def get_data(self):
        img=self.aws_client.get_object(Bucket=self.bucket, Key='_user.png')
        print(img)
        return
    def upload_data(self, file):
        self.aws_client.put_object(Body=file, 
                                   Bucket=self.bucket, 
                                   Key='user.png',
                                   ContentType='image/jpeg'
                                   )
        return 0
    def delete_data(self):
        self.aws_client.delete_object(Bucket=self.bucket, Key='test/test.txt')
        return 0

