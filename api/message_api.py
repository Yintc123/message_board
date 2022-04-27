from flask import *
from dotenv import load_dotenv, dotenv_values
from .aws_api import Aws_s3_api

env=".env" # 執行環境
load_dotenv(override=True)

error={
        "error":True,
        "message":None
}

resp={"ok":True}

app1=Blueprint("message_api", __name__)

url="/message"
@app1.route(url, methods=["POST"])
def send_message():
    message=request.form.get("message")
    img=request.files.get("img").read()
    print(message)
    print(type(img))
    s3=Aws_s3_api()
    result=s3.upload_data(file=img)
    print(result)
    return resp

@app1.route(url, methods=["get"])
def get_message():
    print("hm")
    return resp