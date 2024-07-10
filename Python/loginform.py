from tkinter import*
win=Tk()
value=StringVar()
value1=StringVar()
win.geometry("300x300")
win.maxsize(200,200)
win.minsize(150,150)
list=[]


def Ragister():
    # text=event.widget.cget('text')
    # print(text)
    userid=ent1.get()
    password=ent2.get()
    new_row=[userid,password]
    # value=list.append(new_row)
    print("list=",list)
    userid=""
    password=""

win.title("Registration Form")

a=Label(text="User Id")
a.place(x=1,y=1)

b=Label(text="Passoword")
b.place(x=1,y=30)

ent1=Entry(win)
ent1.place(x=80,y=1)

ent2=Entry(win)
ent2.place(x=80,y=30)

btn1=Button(text="Submit",command=Ragister)
btn1.place(x=70,y=150)
# btn1.bind('<Button-1>',Ragister)


win.mainloop()
