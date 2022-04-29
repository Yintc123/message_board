import mysql.connector
from dotenv import load_dotenv, dotenv_values

env='.env' # 執行環境
load_dotenv(override=True)

mydb=mysql.connector.connect(
    host=dotenv_values(env)["RDS_host"],
    user=dotenv_values(env)["user"],
    password=dotenv_values(env)["password"],
    database="test",
    auth_plugin="mysql_native_password",
    port=dotenv_values(env)["port"],
)

mycursor=mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)
# mycursor.execute("CREATE DATABASE message_board")

# mycursor.execute("CREATE TABLE history_message (id BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT, img_message VARCHAR(255), text_message TEXT NOT NULL, time DATETIME NOT NULL DEFAULT NOW())")

# mycursor.execute("DROP TABLE history_message")

# mycursor.execute("ALTER TABLE history_message ADD name VARCHAR(255) NOT NULL")

query="SELECT*FROM history_message"
mycursor.execute(query)
result=mycursor.fetchall()

for x in result:
    print(x)
