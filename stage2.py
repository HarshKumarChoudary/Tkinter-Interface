from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

root=Tk()
root.title("Catenary Input Interface")
root.geometry("620x650")
notebook=Notebook(root)
notebook.pack(expand=1,fill="both",pady=5,padx=5)

#tabs for different input fields.
tab1=Frame(notebook)
notebook.add(tab1,text="Catenary Data")

tab2=Frame(notebook)
notebook.add(tab2,text="Height Reduction Data")

tab3=Frame(notebook)
notebook.add(tab3,text="Span lengths")

tab4=Frame(notebook)
notebook.add(tab4,text="Supports")

tab5=Frame(notebook)
notebook.add(tab5,text="Stitch wires/Droppers")

#packing all tabs
notebook.pack(expand=1,fill="both")

#tab1 function to generate tab1:

def tab1func():
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

    #labels
    Label(tab1,text='''Catenay Wire Mass''',width=25).grid(row=0,column=0,padx=5,pady=13)
    Label(tab1,text='''Catenary Wire Number''',width=25).grid(row=0,column=2,padx=5,pady=13)
    Label(tab1,text='''Catenary Wire Cross-Sectional Area''',width=25).grid(row=1,column=0,padx=5,pady=13)
    Label(tab1,text='''Catenary Wire tensile force''',width=25).grid(row=1,column=2,padx=5,pady=13)
    Label(tab1,text='''Catenary Wire Material \nProperties''',width=25).grid(row=2,column=0,padx=5,pady=13)

    #Entry Box
    en6 = Entry(tab1,textvariable=var6).grid(row=0,column=1,padx=5,pady=13)
    en2 = Entry(tab1,textvariable=var2).grid(row=0,column=3,padx=5,pady=13)
    en3 = Entry(tab1,textvariable=var3).grid(row=1,column=1,padx=5,pady=13)
    en4 = Entry(tab1,textvariable=var4).grid(row=1,column=3,padx=5,pady=13)
    en5 = Entry(tab1,textvariable=var5).grid(row=2,column=1,padx=5,pady=13)
    

    #button
    btn = Button(tab1,text="Simulate",command=func)
    btn.place(x=300,y=300)


#tab2 function to generate tab2;
def tab2func():

    Label(tab2,text='''Maximum permissible gradient''',width=25).grid(row=0,column=0,padx=5,pady=13)
    mpg=Entry(tab2).grid(row=0,column=1,padx=5, pady=13)

    Label(tab2,text='''Maximum permissible change of gradient''',width=25).grid(row=0,column=2,padx=5,pady=13)
    dmpg=Entry(tab2).grid(row=0,column=3,padx=5, pady=13)

    Label(tab2,text='''Average horizontal dropper distance''',width=25).grid(row=1,column=0,padx=5,pady=13)
    ahdd=Entry(tab2).grid(row=1,column=1,padx=5, pady=13)

    Label(tab2,text='''Maximum Contact wire wear''',width=25).grid(row=1,column=2,padx=5,pady=13)
    mcww=Entry(tab2).grid(row=1,column=3,padx=5, pady=13)

    Label(tab2,text='''Minimum contact wire height''',width=25).grid(row=2,column=0,padx=5,pady=13)
    mcwh=Entry(tab2).grid(row=2,column=1,padx=5, pady=13)

    Label(tab2,text='''Minimum system height''',width=25).grid(row=2,column=2,padx=5,pady=13)
    msh=Entry(tab2).grid(row=2,column=3,padx=5, pady=13)

    Label(tab2,text='''Presag''',width=25).grid(row=3,column=0,padx=5,pady=13)
    pres=Entry(tab2).grid(row=3,column=1,padx=5, pady=13)

    Label(tab2,text='''Minimum vertical length of droppers''',width=25).grid(row=3,column=2,padx=5,pady=13)
    mvld=Entry(tab2).grid(row=3,column=3,padx=5, pady=13)

    Label(tab2,text='''Minimum safety clearance to earthed components''',width=25).grid(row=4,column=0,padx=5,pady=13)
    msec=Entry(tab2).grid(row=4,column=1,padx=5, pady=13)

    Label(tab2,text='''Min. Vert. length of moving droppers''',width=25).grid(row=4,column=2,padx=5,pady=13)
    mvldr=Entry(tab2).grid(row=4,column=3,padx=5, pady=13)

    Label(tab2,text='''Minimum clearance structure to pole''',width=25).grid(row=5,column=0,padx=5,pady=13)
    mcsp=Entry(tab2).grid(row=5,column=1,padx=5, pady=13)

    Label(tab2,text="Pantograph contact force",width=25).grid(row=6,column=0,padx=5,pady=13)
    pcf=Entry(tab2).grid(row=6,column=1,padx=5, pady=13)

    Label(tab2,text='''Minimum permissible span length''',width=25).grid(row=7,column=0,padx=5,pady=13)
    mpsl1=StringVar()
    mpsl=Entry(tab2,textvariable=mpsl1).grid(row=7,column=1,padx=5, pady=13)

    def fun():
        msg=messagebox.showinfo("Success",mpsl1.get())

    btn=Button(tab2,text="Enter",command=fun)
    btn.grid(row=8,column=2)

tab1func()
tab2func()
root.mainloop()