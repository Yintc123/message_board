import database.db_pool as pool

class Handle_message_board_db():
    def __init__(self):
        self.conn=None
        self.cur=None
    
    def connection(self):
        try:
            self.conn=pool.pool.get_connection()
            self.cur=self.conn.cursor(dictionary=True)
            print("successful access to the connection")
        except:
            print("error in the connection")
            
    def close(self):
        try:
            self.cur.close()#cursor.close()釋放從資料庫取得的資源，兩個皆須關閉
            self.conn.close()#connection.close()方法可關閉對連線池的連線，並釋放相關資源
            print("close the connection successfully")
        except:
            print("error in closing the connection")
            
    def get_message(self):
        self.connection()
        query="SELECT*FROM history_message"
        self.cur.execute(query)
        all_message=self.cur.fetchall()
        self.close()
        return all_message
    
    def add_message(self, img_message, text_message, name):
        self.connection()
        query_add_message="INSERT INTO history_message (img_message, text_message, name) VALUES(%s, %s, %s)"
        self.cur.execute(query_add_message, (img_message, text_message, name))
        self.conn.commit()
        self.close()
        return 0 #註冊成功
    
    def get_message_id(self):
        self.connection()
        query_total="SELECT id FROM history_message ORDER BY id DESC LIMIT 1;"
        self.cur.execute(query_total)
        message_id=self.cur.fetchone()
        if message_id==None:
            self.close()
            return 0
        self.close()
        return message_id["id"]
    
    def delete_message_by_id(self, id):
        self.connection()
        query_delete="DELETE FROM history_message WHERE id=%s"
        self.cur.execute(query_delete %id)
        self.conn.commit()
        self.close()
        return 0 #刪除成功