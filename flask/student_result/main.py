from flask import Flask,render_template,redirect,request   
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///result.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Result(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    num = db.Column(db.String,nullable=False)
    std = db.Column(db.String,nullable=False)
    sci = db.Column(db.Integer,nullable=False)
    phy = db.Column(db.Integer,nullable=False)
    maths = db.Column(db.Integer,nullable=False)
    eng = db.Column(db.Integer,nullable=False)
    total = db.Column(db.Integer,nullable=False)
    per = db.Column(db.Integer,nullable=False)
    grade = db.Column(db.String,nullable=False)
    date = db.Column(db.DateTime,default=datetime.now)

    def __repr__(self):
        return f"{self.sno} - {self.name}"
    
@app.route("/", methods=['GET','POST'])
def Home():
    if request.method=='POST':
        name=(request.form['name'])
        num=(request.form['num'])
        std=(request.form['std'])
        sci=float(request.form['sci'])
        phy=float(request.form['phy'])
        maths=float(request.form['maths'])
        eng=float(request.form['eng'])
        total=sci+phy+maths+eng
        totals=float(total)
        per = totals / 4
        if per>=90:
            grade='A'
        elif per>=80:
            grade='B'
        elif per >=70:
            grade='C'
        elif per>=60:
            grade='D'
        else:
            grade='E'
        std_result=Result(name=name,num=num,std=std,phy=phy,sci=sci,maths=maths,eng=eng,total=total,per=per,grade=grade)
        db.session.add(std_result)
        db.session.commit()

    std_result=Result.query.all()
    return render_template("index.html",std_result=std_result)

@app.route("/update/<int:sno>", methods=['GET','POST'])
def Update(sno):
     if request.method=='POST':
        name=(request.form['name'])
        num=(request.form['num'])
        std=(request.form['std'])
        sci=float(request.form['sci'])
        phy=float(request.form['phy'])
        maths=float(request.form['maths'])
        eng=float(request.form['eng'])
        total=sci+phy+maths+eng
        totals=float(total)
        per = totals / 4
        if per>=90:
            grade='A'
        elif per>=80:
            grade='B'
        elif per >=70:
            grade='C'
        elif per>=60:
            grade='D'
        else:
            grade='E'
        std_result=Result.query.filter_by(sno=sno).first()
        std_result.name=name
        std_result.num=num
        std_result.std=std
        std_result.sci=sci
        std_result.phy=phy
        std_result.maths=maths
        std_result.eng=eng
        std_result.total=total
        std_result.per=per
        std_result.grade=grade
        return redirect("/")
     std_result=Result.query.filter_by(sno=sno).first()
     return render_template("update.html",std_result=std_result)

@app.route("/delete/<int:sno>", methods=['GET','POST'])
def Delete(sno):
    std_result=Result.query.filter_by(sno=sno).first()
    db.session.delete(std_result)
    db.session.commit()
    return redirect("/")
        

if __name__ =="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=7000)