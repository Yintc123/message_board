import mysql.connector
from dotenv import load_dotenv, dotenv_values

env='.env' # 執行環境
load_dotenv(override=True)

mydb=mysql.connector.connect(
    host=dotenv_values(env)["RDS_host"],
    user=dotenv_values(env)["user"],
    password=dotenv_values(env)["password"],
    database="message_board",
    auth_plugin="mysql_native_password",
    port=dotenv_values(env)["port"],
)

mycursor=mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)
# mycursor.execute("CREATE DATABASE message_board")

mycursor.execute("CREATE TABLE history_message (id BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT, img_id BIGINT, text_message TEXT NOT NULL, time DATETIME NOT NULL DEFAULT NOW())")
mycursor.execute("CREATE TABLE history_img (id BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT, img_name VARCHAR(255) NOT NULL, img_file LONGTEXT NOT NULL, time DATETIME NOT NULL DEFAULT NOW())")

mycursor.execute("ALTER TABLE history_message ADD name VARCHAR(255) NOT NULL")
# mycursor.execute("ALTER TABLE history_message ADD FOREIGN KEY (img_id) REFERENCES history_img(id)")

# mycursor.execute("DROP TABLE history_message")
# mycursor.execute("DROP TABLE history_img")

# query="SELECT*FROM history_message"
# mycursor.execute(query)
# result=mycursor.fetchall()

# for x in result:
#     print(x)

# query="SELECT*FROM history_img"
# query="DESCRIBE history_message"
# query="SHOW TABLES"
# result=mycursor.execute(query)
# result=mycursor.fetchall()

# print(mycursor)

# for i in mycursor:
#     print(i)

# print(result)



