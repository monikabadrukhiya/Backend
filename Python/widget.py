from tkinter import*
win=Tk()
equation=StringVar()    #special variable used in tkinter to hold string value


a=Label(text="Calculator")
a.place(x=1,y=1)

b=Entry(textvariable=equation)
b.place(x=1,y=20)

#  for click button
def Btn_click(event):
   text=event.widget.cget('text')
   print(text)
   ans=b.get()
   equation.set(ans)
   b.update()
   if text=="=":
        ans=b.get()
        total=str(eval(ans))
        equation.set(total)
        b.update()
   elif text=="AC":
     equation.set("")
   elif text=="D":
      ans=ans[:-1]
      equation.set(ans)
      b.update()
   else:
      ans=b.get()
      equation.set(ans+text)
      b.update()

# layout of calculator
win.geometry("200x200")
win.maxsize(300,300)
win.minsize(120,120)
# win.resizable()


# placing the Buttons & on clickeble buttons event
c=Button(text='AC')
c.place(x=1,y=40)   
c.bind('<Button-1>',Btn_click)

d=Button(text='%')
d.place(x=30,y=40)
d.bind('<Button-1>',Btn_click)

e=Button(text='D')
e.place(x=60,y=40)
e.bind('<Button-1>',Btn_click)

f=Button(text='/')
f.place(x=90,y=40)
f.bind('<Button-1>',Btn_click)

g=Button(text='7')
g.place(x=1,y=70)
g.bind('<Button-1>',Btn_click)

h=Button(text='8')
h.place(x=30,y=70)
h.bind('<Button-1>',Btn_click)

i=Button(text='9')
i.place(x=60,y=70)
i.bind('<Button-1>',Btn_click)

j=Button(text='*')
j.place(x=90,y=70)
j.bind('<Button-1>',Btn_click)

k=Button(text='4')
k.place(x=1,y=100)
k.bind('<Button-1>',Btn_click)

l=Button(text='5')
l.place(x=30,y=100)
l.bind('<Button-1>',Btn_click)

m=Button(text='6')
m.place(x=60,y=100)
m.bind('<Button-1>',Btn_click)

n=Button(text='-')
n.place(x=90,y=100)
n.bind('<Button-1>',Btn_click)

o=Button(text='1')
o.place(x=1,y=130)
o.bind('<Button-1>',Btn_click)

p=Button(text='2')
p.place(x=30,y=130)
p.bind('<Button-1>',Btn_click)

q=Button(text='3')
q.place(x=60,y=130)
q.bind('<Button-1>',Btn_click)

r=Button(text='+')
r.place(x=90,y=130)
r.bind('<Button-1>',Btn_click)

s=Button(text='00')
s.place(x=1,y=160)
s.bind('<Button-1>',Btn_click)

t=Button(text='0')
t.place(x=30,y=160)
t.bind('<Button-1>',Btn_click)

u=Button(text='.')
u.place(x=60,y=160)
u.bind('<Button-1>',Btn_click)

v=Button(text='=')
v.place(x=90,y=160)
v.bind('<Button-1>',Btn_click)

win.mainloop()
