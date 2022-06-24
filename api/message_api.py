import base64
import datetime, time
from flask import *
from dotenv import load_dotenv, dotenv_values
from .aws_api import Aws_s3_api
from database.message_board_db import Handle_message_board_db as db
from flask_cors import CORS

env=".env" # 執行環境
load_dotenv(override=True)

error={
        "error":True,
        "message":None
}

resp={"ok":True}

app1=Blueprint("message_api", __name__)
CORS(app1)

url="/message"
@app1.route(url, methods=["POST"])
def send_message():
    resp={"id":None}
    message=request.form.get("message")
    name=request.form.get("name")
    img=request.files.get("img")
    img_file=None
    img_filename=None
    message_db=db()
    if img:
        img_file=img.read()
        img_format=img.filename.split(".")[1]
        previous_img=message_db.find_img(base64.b64encode(img_file).decode("utf-8"))
        if not previous_img:
            s3=Aws_s3_api()
            # 由於時間不會重複，圖片以時間命名，以免使用cdn系統抓到同名但內容的圖片
            timeString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            img_filename=s3.upload_data(img_file, img_format, timeString)
        img_file=base64.b64encode(img_file).decode("utf-8") # 將Blob以base64轉成text檔以利存檔於mysql
    message_db.add_message(img_filename, img_file, message, name)
    message_id=message_db.get_message_id()
    resp["id"]=message_id
    return resp

@app1.route(url, methods=["get"])
def get_message():
    message_db=db()
    history_message=message_db.get_message()
    resp={"history":[]}
    for index in history_message:
        message={}
        img_url=None
        if index["img_id"] != 0:
            img_filename=message_db.find_img_by_id(index["img_id"])
            img_url=dotenv_values(env)["url_cdn"]+img_filename
        message["text_message"]=index["text_message"]
        message["img_url"]=img_url
        message["name"]=index["name"]
        message["id"]=index["id"]
        resp["history"].append(message)
    return resp

@app1.route(url, methods=["DELETE"])
def delete_message():
    message_id=request.form.get("id")
    # print(message_id)
    message_db=db()
    message_db.delete_message_by_id(message_id)
    return resp