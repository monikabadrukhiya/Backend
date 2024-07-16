from tkinter import*
win=Tk()
current=""

win.geometry("200x200")
win.maxsize(200,200)
win.minsize(150,150)

def get_btn_text(event):
    text=event.widget.cget('text')
    print("Event : ",text)
    current = text

    
def set_btn_text(event):
    text=event.widget.cget('text')
    print("Text= : ",text)
    # if text == "":
    #     pass
    
    
win.title("Tic Tac Toe")

btn1=Button(win,text="")
btn1.place(x=1,y=10)
btn1.bind('<Button-1>',set_btn_text)

btn2=Button(win,text="")
btn2.place(x=20,y=10)
btn2.bind('<Button-1>',set_btn_text)


btn3=Button(win,text="")
btn3.place(x=40,y=10)
btn3.bind('<Button-1>',set_btn_text)

btn4=Button(win,text="")
btn4.place(x=1,y=40)
btn4.bind('<Button-1>',set_btn_text)

btn5=Button(win,text="")
btn5.place(x=20,y=40)
btn5.bind('<Button-1>',set_btn_text)

btn6=Button(win,text="")
btn6.place(x=40,y=40)
btn6.bind('<Button-1>',set_btn_text)

btn7=Button(win,text="")
btn7.place(x=1,y=80)
btn7.bind('<Button-1>',set_btn_text)

btn8=Button(win,text="")
btn8.place(x=20,y=80)
btn8.bind('<Button-1>',set_btn_text)

btn9=Button(win,text="")
btn9.place(x=40,y=80)
btn9.bind('<Button-1>',set_btn_text)

btnx=Button(win,text="X")
btnx.place(x=40,y=120)
btnx.bind('<Button-1>',get_btn_text)

btnO=Button(win,text="O")
btnO.place(x=60,y=120)
btnO.bind('<Button-1>',get_btn_text)

win.mainloop()