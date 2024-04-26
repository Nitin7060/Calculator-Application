from tkinter import *
import tkinter.messagebox as tms

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value="Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()




root = Tk()
root.geometry('600x900')
# Gui app title name
root.title("Magic Calculator")
# paste app icon
root.wm_iconbitmap('calculator_icon.ico')
# for background sheet color
root.configure(bg='orange')

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar = scvalue ,font= "lucida 40  bold",bg="sky blue")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f1 = Frame(root,bg='blue')
f1.pack()

b1 = Button(f1,text="9",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=25,pady=18)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="8",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=25,pady=18)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="7",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=25,pady=18)
b1.bind("<Button-1>", click)


f1 = Frame(root,bg='blue')
f1.pack()
b1 = Button(f1,text="6",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=25,pady=18)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="5",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=25,pady=18)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="4",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=25,pady=18)
b1.bind("<Button-1>", click)


f1 = Frame(root,bg='blue')
f1.pack()
b1 = Button(f1,text="3",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=25,pady=18)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="2",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=25,pady=18)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="1",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=25,pady=18)
b1.bind("<Button-1>", click)


f1 = Frame(root,bg='blue')
f1.pack()
b1 = Button(f1,text="0",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=24,pady=18)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="%",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=24,pady=18)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="*",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=24,pady=18)
b1.bind("<Button-1>", click)


f1 = Frame(root,bg='blue')
f1.pack()
b1 = Button(f1,text="+",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=27,pady=18)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="-",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=27,pady=18)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="/",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=27,pady=18)
b1.bind("<Button-1>", click)


f1 = Frame(root,bg='blue')
f1.pack()
b1 = Button(f1,text="C",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=21,pady=18)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="00",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=21,pady=18)
b1.bind("<Button-1>", click)
b1 = Button(f1,text="=",padx=40,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=21,pady=18)
b1.bind("<Button-1>", click)

root.mainloop()