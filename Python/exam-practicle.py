list=[]
from tkinter import*
win=Tk()
value=StringVar()
value1=StringVar()
value2=StringVar()
value3=StringVar()
value4=StringVar()
value5=StringVar()
value6=StringVar()
value7=StringVar()
value8=StringVar()
value9=StringVar()
# value10=StringVar()
# value11=StringVar()

win.geometry("700x700")
win.maxsize(400,400)
win.minsize(200,200)
def Btn_click():
        name=ent1.get()
        print("name=",name)
        lname=ent2.get()
        print("lname=",lname)
        age=ent3.get()
        num=ent4.get()
        # hobby=ent5.get()
        dob=ent6.get()
        qualification=ent7.get()
        userid=ent8.get()
        password=ent9.get()
        sname=ent10.get()
        # age=ent11.get()
        # num=ent12.get()
        
        data=[name,lname,sname,dob,qualification,userid,password,age,num]
        list.append(data)
        print("list=",list)

win.title("Registration Form")

l1=Label(text="Name")
l1.place(x=1,y=1)

ent1=Entry(win,textvariable=value)
ent1.place(x=100,y=1)

l2=Label(text="last Name")
l2.place(x=1,y=30)

ent2=Entry(win,textvariable=value1)
ent2.place(x=100,y=30)

l10=Label(text="Surname")
l10.place(x=1,y=60)

ent10=Entry(win,textvariable=value2)
ent10.place(x=100,y=60)

l3=Label(text="Age")
l3.place(x=1,y=90)

ent3=Entry(win,textvariable=value3)
ent3.place(x=100,y=90)


l4=Label(text="Number")
l4.place(x=1,y=120)

ent4=Entry(win,textvariable=value4)
ent4.place(x=100,y=120)

l5=Label(text="Hobby")
l5.place(x=1,y=150)
var2=IntVar()
Checkbutton(win,text="Dance",width=20,font=('bold',10)).place(x=40,y=150)
Checkbutton(win,text="Singing",width=20,font=('bold',10)).place(x=160,y=150)
# Checkbutton(win,text="Reading",width=20,font=('bold',10)).place(x=130,y=150)
# Checkbutton(win,text="Communication",width=20,font=('bold',10)).place(x=220,y=150)
# ent5=Entry(win,textvariable=value5)
# ent5.place(x=100,y=150)

l6=Label(text="DOB")
l6.place(x=1,y=180)

ent6=Entry(win,textvariable=value6)
ent6.place(x=100,y=180)

l7=Label(text="Qualification")
l7.place(x=1,y=210)

ent7=Entry(win,textvariable=value7)
ent7.place(x=100,y=210)

l8=Label(text="user Id")
l8.place(x=1,y=240)

ent8=Entry(win,textvariable=value8)
ent8.place(x=100,y=240)

l9=Label(text="Password")
l9.place(x=1,y=260)

ent9=Entry(win,textvariable=value9)
ent9.place(x=100,y=260)

l11=Label(text="Gender")
l11.place(x=1,y=290)

radiobtn = IntVar()  
Radiobutton(win, text="Male",padx = 5, variable=radiobtn, value=1).place(x=100,y=290)  
Radiobutton(win, text="Female",padx = 20, variable=radiobtn, value=2).place(x=150,y=290)  
Radiobutton(win, text="Other",padx = 20, variable=radiobtn, value=2).place(x=230,y=290)

list_of_cntry = ("Surat", "Bhavanagar", "Ahemdabad", "Rajkot","Hydrabad")  
cv = StringVar()  
drplist= OptionMenu(win, cv, *list_of_cntry)  
drplist.config(width=15)  
cv.set("Select  city")  

l12=Label(text="Select City")
l12.place(x=1,y=320)
drplist.place(x=100,y=320)

# ent12=Entry(win,textvariable=value11)
# ent12.place(x=100,y=320)

btn=Button(text="Submit",command=Btn_click)
btn.place(x=100,y=370)

win.mainloop()