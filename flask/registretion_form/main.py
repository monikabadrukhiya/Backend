from flask import Flask,redirect,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///ragister.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False  
db=SQLAlchemy(app)

class Ragister(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    num = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    pwd = db.Column(db.String(200),nullable=False)
    date = db.Column(db.DateTime,default=datetime.now)

    def __repr__(self):
        return f"{self.sno} - {self.name}"


@app.route("/",methods=['GET','POST'])
def Home():
    if request.method=='POST':
        name=request.form['name']
        num=request.form['num']
        email=request.form['email']
        pwd=request.form['pwd']

        alldata=Ragister(name=name,num=num,email=email,pwd=pwd)
        db.session.add(alldata)
        db.session.commit()
    alldata=Ragister.query.all()
    return render_template("index.html",alldata=alldata)

@app.route("/update/<int:sno>",methods=['GET','POST'])
def Update(sno):
    if request.method =='POST':
        name=request.form['name']
        num=request.form['num']
        email=request.form['email']
        pwd=request.form['pwd']
        data=Ragister.query.filter_by(sno=sno).first()

        data.name=name
        data.num=num
        data.email=email
        data.pwd=pwd
        db.session.add(data)
        db.session.commit()
        return redirect("/")

    data=Ragister.query.filter_by(sno=sno).first()
    return render_template("update.html",data=data)

@app.route("/delete/<int:sno>")
def Delete(sno):
    data=Ragister.query.filter_by(sno=sno).first()
    db.session.delete(data)
    db.session.commit()
    return redirect("/")




 