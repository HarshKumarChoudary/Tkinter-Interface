from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#window
win = Tk()

#Variables
var2 = StringVar()
var3 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()

def func():
    val2 = var2.get()
    val3 = var3.get()
    val4 = var4.get()
    val5 = var5.get()
    val6 = var6.get()
    if val3 == "" or val2 == "" or val5 == "" or val4 == "" or val6 == "":
        messagebox.showwarning("Some values are not entered")
    else:
        messagebox.showinfo("All values are entered Successfully")

    
win.title("Catenary Input")
win.iconbitmap("Awicons-Vista-Artistic-2-Hot-Train.ico")
win.maxsize(width=600,height=600)
win.minsize(width=300,height=300)
win.geometry("500x500")

#labels

l1 = Label(win, text = "This is Input Interface for Catenary System",bg="red",fg="white",width=600)
l1.pack()
l2 = Label(win,text="Maximum Permissible Gradient")
l3 = Label(win,text="Maximum Permissible Change of Gradient")
l4 = Label(win,text="Pantograph Contact Force")
l5 = Label(win,text="Minimum Permissible Span Length")
l6 = Label(win,text="Minimum System Height")

l2.place(x=10,y=40)
l3.place(x=10,y=80)
l4.place(x=10,y=120)
l5.place(x=10,y=160)
l6.place(x=10,y=200)

#Entry Box
en6 = Entry(win,bd=5,textvariable=var6)
en6.place(x=300,y=200)
en2 = Entry(win,bd=5,textvariable=var2)
en2.place(x=300,y=40)
en3 = Entry(win,bd=5,textvariable=var3)
en3.place(x=300,y=80)
en4 = Entry(win,bd=5,textvariable=var4)
en4.place(x=300,y=120)
en5 = Entry(win,bd=5,textvariable=var5)
en5.place(x=300,y=160)

#button
btn = Button(win,text="Simulate",bg="yellow",command=func)
btn.place(x=250,y=250)

win.mainloop()
