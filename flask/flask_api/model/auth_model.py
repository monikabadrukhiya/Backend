import pymysql
import json
from flask import make_response,request
from functools import wraps
import jwt
import re   #regular expresion
from config.config import dbconfig


class auth_model():
    def __init__(self):
        try:
            self.con = pymysql.connect(host=dbconfig['hostname'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'],cursorclass=pymysql.cursors.DictCursor )
            # self.con.autocommit=True
            self.cur=self.con.cursor()
            print("connection succesfully")
        except:
            print("some error")

    def token_auth(self, endpoint=""):
        def inner1(func):
            @wraps(func)
            def inner2(*args):
                endpoint=request.url_rule
                print(endpoint)
                authorization=request.headers.get("authorization")
                if re.match("^bearer *([^ ]+) *$",authorization ,flags=0):
                    tokan=authorization.split(" ")[1]
                    try:
                        jwt_token=jwt.decode(tokan ,"moni", algorithms="HS256")
                    except jwt.ExpiredSignatureError:
                        return make_response({"ERROR":"TOKEN_EXPIRED"},401)
                    role_id=jwt_token['payload']['role_id']
                    self.cur.execute(f"SELECT roles FROM accessibility_view WHERE endpoint='{endpoint}'")
                    result=self.cur.fetchall()
                    if len(result)>0:
                        allowed_roles=json.loads((result[0]['roles']))
                        if role_id in allowed_roles:
                            return func(*args)
                        else:
                             return make_response({"ERROR":"UNKNOWN_roles"}, 404)
                    else:
                        return make_response({"ERROR":"UNKNOWN_ENDPOINT"}, 404)
                else:
                    return make_response({"ERROR":"INVALID_TOKEN"}, 401)
            return inner2
        return inner1