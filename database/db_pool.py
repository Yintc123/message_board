from mysql.connector.pooling import MySQLConnectionPool
from dotenv import load_dotenv, dotenv_values

env=str('.env.'+dotenv_values('.env')['MODE']) # 執行環境
load_dotenv(override=True)

pool=MySQLConnectionPool(
    host="localhost",
    user="root",
    password=dotenv_values(env)["mysql_password"],
    database="message_board",
    pool_name="myPool",
    pool_size=20,
    auth_plugin="mysql_native_password",
    port=dotenv_values(env)["mysql_port"]
)