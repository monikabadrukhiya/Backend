from app import app
from model.user_model import user_model
from model.auth_model import auth_model
from flask import request,send_file
from datetime import datetime
obj=user_model()
auth=auth_model()

@app.route("/user/readalldata")
@auth.token_auth()
def user_readalldata_ctrlr():
    return obj.user_readalldata_model()

@app.route("/user/adddata",methods=["POST"])
@auth.token_auth()
def user_adddata_ctrlr():
    return obj.user_adddata_model(request.form)

@app.route("/user/addmultiple",methods=["POST"])
def user_add_multiple_ctrlr():
    return obj.user_add_multiple_model(request.json)

@app.route("/user/update",methods=["PUT"])
def user_update_ctrlr():
    return obj.user_update_model(request.form)

@app.route("/user/delete/<id>",methods=["DELETE"])
def user_delete_ctrlr(id):
    return obj.user_delete_model(id)

@app.route("/user/patch/<id>",methods=["PATCH"])
def user_patch_ctrlr(id):
    return obj.user_patch_model(request.form, id)

@app.route("/user/getall/limit/<limit>/page/<page>",methods=["GET"])
def user_pagination_ctrlr(limit,page):
    return obj.user_pagination_model(limit,page)

@app.route("/user/<uid>/upload/avatar",methods=["PUT"])
def user_upload_avatar_ctrlr(uid):
    file=request.files['avatar']
    uniqefilename=str(datetime.now().timestamp()).replace(".","")
    splitfile=file.filename.split(".")
    extension=splitfile[len(splitfile)-1]
    finalfilepath=f"upload/{uniqefilename}.{extension}"
    file.save(finalfilepath)

    return obj.user_upload_avatar_ctrlr(uid,finalfilepath)

@app.route("/upload/<filename>") 
def user_getavatar_ctrlr(filename):
    return send_file(f"upload/{filename}")

@app.route("/user/login",methods=["POST"])
def user_login_ctrlr():
    return obj.user_login_model(request.form)
    
    