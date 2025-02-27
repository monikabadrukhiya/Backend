import pymysql
import json
from flask import make_response
from datetime import datetime,timedelta
import jwt
from config.config import dbconfig
class user_model():
    def __init__(self):
        try:
            self.con = pymysql.connect(host=dbconfig['hostname'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'],cursorclass=pymysql.cursors.DictCursor )
            # self.con.autocommit=True
            self.cur=self.con.cursor()
            print("connection succesfully")
        except:
            print("some error")
    def user_readalldata_model(self):
        self.cur.execute("SELECT * FROM users")
        result=self.cur.fetchall()    #all data show karvamate
        # print(result)
        if len(result)>0:
            # return json.dumps(result)  #json formnat ma conver karu
            response=make_response({"payload":result},200)
            response.headers['Access-Control-Allow-Origin']="*"
            return response
        else:
            return make_response({"message":"no data found"},204)
        
    def user_adddata_model(self,data):
        query = "INSERT INTO users (name, email, phone, password,role_id) VALUES (%s, %s, %s, %s, %s)"
        values = (data['name'], data['email'], data['phone'], data['password'], data['role_id'])
        self.cur.execute(query, values)  
        self.con.commit()
        return make_response({"message": "User created successfully"},201)
    
    def user_add_multiple_model(self,data):
        query = "INSERT INTO users (name, email, phone, password,role_id) VALUES "
        for userdata in data:
            query += f"('{userdata['name']}', '{userdata['email']}', '{userdata['phone']}', '{userdata['password']}', {userdata['role_id']}),"
        finalqry = query.rstrip(",")
        self.cur.execute(finalqry)  
        self.con.commit()
        return make_response({"message": "MULTIPLE_USER_CREATED"},201)
    
    def user_update_model(self,data):
        query = """ UPDATE users  SET name = %s, email = %s, phone = %s, password = %s, role_id=%s
        WHERE id = %s"""
        values = (data['name'], data['email'], data['phone'], data['password'],data['role_id'], data['id'])
        self.cur.execute(query, values)  
        self.con.commit()
        if self.cur.rowcount>0:
            return make_response({"message": "User update successfully"},201)
        else:
            return make_response({"message":"nothing to update"},202)
        
    def user_delete_model(self,id):
        query = "DELETE FROM users WHERE id=%s"
        values = id
        self.cur.execute(query, values)  
        self.con.commit()
        if self.cur.rowcount>0:
            return make_response({"message": "User delete successfully"},200)
        else:
            return make_response({"message":"nothing to delete"},202)
        
    def user_patch_model(self,data,id):
        query = " UPDATE users  SET "
        for key in data:
            query=query+f"{key}='{data[key]}',"
        query=query[:-1] + f" WHERE id={id}"
        self.cur.execute(query)  
        if self.cur.rowcount>0:
            return make_response({"message": "User update successfully"},201)
        else:
            return make_response({"message":"nothing to update"},202)
    
    def user_pagination_model(self,limit,page):
        limit=int(limit)
        page=int(page)
        start=(page*limit)-limit
        query=f"SELECT * FROM users LIMIT {start},{limit}"
        self.cur.execute(query)
        result=self.cur.fetchall()    #all data show karvamate
        if len(result)>0:
            response=make_response({"payload":result},200)
            return response
        else:
            return make_response({"message":"no data found"},204)
        
    def user_upload_avatar_ctrlr(self,id,filepath):
        self.cur.execute(f"UPDATE users SET avatar='{filepath}' WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message": "file uploaded successfully"},201)
        else:
            return make_response({"message":"nothing to update"},202)
        

    def user_login_model(self,data):
        query = "SELECT id, name, email, phone, password, avatar, role_id FROM users WHERE email=%s AND password=%s"
        self.cur.execute(query, (data['email'], data['password']))
        result = self.cur.fetchall()
        userdata=result[0]
        exp_time=datetime.now() + timedelta(minutes=15)
        exp_epoch_time=int(exp_time.timestamp())
        payload={
            "payload":userdata,
            "exp":exp_epoch_time
        }
        jwtoken=jwt.encode(payload,"moni", algorithm="HS256")
        return make_response({"token":jwtoken}, 200)
