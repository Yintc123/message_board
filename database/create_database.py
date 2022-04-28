import mysql.connector
from dotenv import load_dotenv, dotenv_values

env=str('.env.'+dotenv_values('.env')["MODE"]) # 執行環境
load_dotenv(override=True)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=dotenv_values(env)['mysql_password'],
    database="message_board",
    auth_plugin="mysql_native_password",
    port=dotenv_values(env)['mysql_port'],
)

mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE message_board")

mycursor.execute("CREATE TABLE history_message (id BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT, img_message VARCHAR(255), text_message TEXT NOT NULL, time DATETIME NOT NULL DEFAULT NOW())")

# mycursor.execute("DROP TABLE history_message")
