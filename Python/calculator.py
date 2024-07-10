from tkinter import*
win=Tk()
current=""
equation=StringVar()    #special variable used in tkinter to hold string value

#  for click button
def Btn_click(item):
    global current
    current=b.get()
    current=current+str(item)
    print(current)
    equation.set(current)

# for clear value
def Btn_clear():
    equation.set("")

# for result
def Btn_equal():
    try:
        global current
        result=str(eval(current))
        print("result=",result)
        equation.set(result)
        current=" "
    except:
        equation.set("error")
        current=""

# for delete last 1 value
def Btn_delete():
    global current
    current=current[:-1]
    equation.set(current)

# layout of calculator
win.geometry("200x200")
win.maxsize(300,300)
win.minsize(120,120)
# win.resizable()


# placing the Buttons & on clickeble buttons event
a=Label(text="Calculator")
a.place(x=1,y=1)

b=Entry(win,textvariable=equation)
b.place(x=1,y=20)

c=Button(win,text='AC',command=lambda: Btn_clear())
c.place(x=1,y=40)   

d=Button(win,text='%',command=lambda:Btn_click("%"))
d.place(x=30,y=40)

e=Button(win,text='D',command=lambda:Btn_delete())
e.place(x=60,y=40)

f=Button(win,text='/',command=lambda:Btn_click("/"))
f.place(x=90,y=40)

g=Button(win,text='7',command=lambda:Btn_click(7))
g.place(x=1,y=70)

h=Button(win,text='8',command=lambda:Btn_click(8))
h.place(x=30,y=70)

i=Button(win,text='9',command=lambda:Btn_click(9))
i.place(x=60,y=70)

j=Button(win,text='*',command=lambda:Btn_click("*"))
j.place(x=90,y=70)

k=Button(win,text='4',command=lambda:Btn_click(4))
k.place(x=1,y=100)

l=Button(win,text='5',command=lambda:Btn_click(5))
l.place(x=30,y=100)

m=Button(win,text='6',command=lambda:Btn_click(6))
m.place(x=60,y=100)

n=Button(win,text='-',command=lambda:Btn_click("-"))
n.place(x=90,y=100)

o=Button(win,text='1',command=lambda:Btn_click(1))
o.place(x=1,y=130)

p=Button(win,text='2',command=lambda:Btn_click(2))
p.place(x=30,y=130)

q=Button(win,text='3',command=lambda:Btn_click(3))
q.place(x=60,y=130)

r=Button(win,text='+',command=lambda:Btn_click("+"))
r.place(x=90,y=130)

s=Button(win,text='00',command=lambda:Btn_click(00))
s.place(x=1,y=160)

t=Button(win,text='0',command=lambda:Btn_click(0))
t.place(x=30,y=160)

u=Button(win,text='.',command=lambda:Btn_click("."))
u.place(x=60,y=160)

v=Button(win,text='=',command=lambda:Btn_equal())
v.place(x=90,y=160)

win.mainloop()
