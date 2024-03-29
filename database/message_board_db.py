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
        except Exception as e:
            print("error in the connection")
            return e
            
    def close(self):
        try:
            self.cur.close()#cursor.close()釋放從資料庫取得的資源，兩個皆須關閉
            self.conn.close()#connection.close()方法可關閉對連線池的連線，並釋放相關資源
            print("close the connection successfully")
        except Exception as e:
            print("error in closing the connection")
            return e
            
    def get_message(self):
        try:
            self.connection()
            query="SELECT*FROM history_message"
            self.cur.execute(query)
            all_message=self.cur.fetchall()
            self.close()
            return all_message
        except Exception as e:
            self.close()
            return e

    def add_img(self, img_name, img_b64):
        try:
            if not img_b64:
                return 0 #無圖片
            img=self.find_img(img_b64)
            if img:
                return 1 #已有圖片
            self.connection()
            query_add_img="INSERT INTO history_img (img_name, img_file) VALUES(%s, %s)"
            self.cur.execute(query_add_img, (img_name, img_b64))
            self.conn.commit()
            self.close()
            return 2 #圖片加入成功
        except Exception as e:
            self.close()
            return e
    
    def add_message(self, img_filename, img_b64, text_message, name):
        try:
            img_id=0
            result=self.add_img(img_filename, img_b64)
            if result!=0:
                img=self.find_img(img_b64)
                img_id=img["id"]
            self.connection()
            query_add_message="INSERT INTO history_message (img_id, text_message, name) VALUES(%s, %s, %s)"
            self.cur.execute(query_add_message, (img_id, text_message, name))
            self.conn.commit()
            self.close()
            return 0 #訊息加入成功
        except Exception as e:
            self.close()
            return e
    
    def get_message_id(self):
        try:
            self.connection()
            query_total="SELECT id FROM history_message ORDER BY id DESC LIMIT 1;"
            self.cur.execute(query_total)
            message_id=self.cur.fetchone()
            if message_id==None:
                self.close()
                return 0
            self.close()
            return message_id["id"]
        except Exception as e:
            self.close()
            return e
    
    def delete_message_by_id(self, id):
        try:
            self.connection()
            query_delete="DELETE FROM history_message WHERE id=%s"
            self.cur.execute(query_delete %id)
            self.conn.commit()
            self.close()
            return 0 #刪除成功
        except Exception as e:
            self.close()
            return e

    def find_img(self, img_b64):
        try:
            self.connection()
            query_img="SELECT*FROM history_img WHERE img_file LIKE %s"
            self.cur.execute(query_img, ("%"+img_b64+"%", ))
            img=self.cur.fetchone()
            self.close()
            return img
        except Exception as e:
            self.close()
            return e

    def find_img_by_id(self, img_id):
        try:
            self.connection()
            query_img="SELECT img_name FROM history_img WHERE id=%s"
            self.cur.execute(query_img %img_id)
            img=self.cur.fetchone()
            self.close()
            return img["img_name"]
        except Exception as e:
            self.close()
            return e