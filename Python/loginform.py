list=[]
list1=[]
name=input("Enter name=")
userid=input("Enter userid=")
password=input("enter password=")
new_row=[name,userid,password]
list.append(new_row)
print("list=",list)


from tkinter import*
win=Tk()
value=StringVar()
value1=StringVar()
value2=StringVar()
win.geometry("300x300")
win.maxsize(200,200)
win.minsize(150,150)

def Login():
    name=ent1.get()
    userid=ent2.get()
    password=ent3.get()
    new_row=[name,userid,password]
    list1.append(new_row)
    
    if list==list1:
        print("login succesfully")
    else:
        print("Go Back")
    value.set("")
    value1.set("")
    value2.set("")

win.title("Registration Form")

a=Label(text="Name")
a.place(x=1,y=1)

a=Label(text="User Id")
a.place(x=1,y=30)

b=Label(text="Passoword")
b.place(x=1,y=60)

ent1=Entry(win,textvariable=value)
ent1.place(x=80,y=1)

ent2=Entry(win,textvariable=value1)
ent2.place(x=80,y=30)

ent3=Entry(win,textvariable=value2)
ent3.place(x=80,y=60)

btn1=Button(text="Login",command=Login)
btn1.place(x=80,y=100)

win.mainloop()
