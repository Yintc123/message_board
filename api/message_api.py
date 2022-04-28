from flask import *
from dotenv import load_dotenv, dotenv_values
from .aws_api import Aws_s3_api
from database.message_board_db import Handle_message_board_db as db

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
    img_url=None
    message_db=db()
    message_id=message_db.get_message_id()
    s3=Aws_s3_api()
    if img:
        img_url=s3.upload_data(img.read(), img.filename.split(".")[1], message_id)
    result=message_db.add_message(img_url, message)
    if result!=0:
        return error
    return resp

@app1.route(url, methods=["get"])
def get_message():
    s3=Aws_s3_api()
    message_db=db()
    history_message=message_db.get_message()
    resp={"history":[]}
    for index in history_message:
        message={}
        img_url=None
        if index["img_message"]:
            img_url=s3.get_data_url(index["img_message"])
        message["text_message"]=index["text_message"]
        message["img_url"]=img_url
        resp["history"].append(message)
    return resp