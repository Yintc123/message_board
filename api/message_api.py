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
    img=request.files.get("img")
    print(message)
    print(img.filename)
    s3=Aws_s3_api()
    result=s3.upload_data(img.read(), img.filename.split(".")[1], 2)
    print(result)
    return resp

@app1.route(url, methods=["get"])
def get_message():
    history_message={
        "text":None,
        "img":None
    }
    s3=Aws_s3_api()
    url=s3.get_data_url()
    history_message["img"]=url
    return history_message