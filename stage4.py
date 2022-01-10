from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os

Master = Tk()

type_of_wire = StringVar()
Master.geometry("300x300")
labelm = Label(Master, text ="Please Select the type of wire you want to use")
 
labelm.pack(pady = 10)
values = {"AC Simple" : "1",
          "AC Stitched" : "2",
          "DC wire" : "3",
          }
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(Master, text = text, variable = type_of_wire,
                value = value).pack(fill = X, ipady = 5)

def newWindow():
    
    # print(type_of_wire.get())
    root=Toplevel(Master)
    root.title("Catenary Input Interface")
    root.geometry("700x700")
    notebook=Notebook(root)
    notebook.pack(expand=1,fill="both",pady=5,padx=5)

    #tabs for different input fields.
    tab1=Frame(notebook)
    notebook.add(tab1,text="Droppers")

    tab2=Frame(notebook)
    notebook.add(tab2,text="Geometrical Arrangement")

    tab3=Frame(notebook)
    notebook.add(tab3,text="Contact Wires")

    tab4=Frame(notebook)
    notebook.add(tab4,text="Messenger Wires")

    tab5=Frame(notebook)
    notebook.add(tab5,text="Stitch Wire")

    tab6=Frame(notebook)
    notebook.add(tab6,text="Steady Arm/Contact Wire Support")

    tab7=Frame(notebook)
    notebook.add(tab7,text="Messenger Wire Support")

    #packing all tabs
    notebook.pack(expand=1,fill="both")

    #tab1 function to generate tab1:

    def tab1func():
        var2 = StringVar()
        var3 = StringVar()
        var6 = StringVar()
        var4 = StringVar()
        var5 = StringVar()
        var1 = StringVar()

        def func():
            val2 = var2.get()
            val3 = var3.get()
            val4 = var4.get()
            val5 = var5.get()
            val1 = var1.get()
            if val3 == "" or val2 == "" or val5 == "" or val4 == "" or val1 == "":
                messagebox.showwarning("Some values are not entered")
            else:
                complete_file_to_write = open("Inputs_Droppers.txt","w+")
                list_of_items = [['Stiffness for tension',val1],['Stiffness for Compression',val2],['Clamp on catenary wire',val3],['Clamp on Contact wire',val4],['Mass per unit length',val5]]
                for items in list_of_items :
                    complete_file_to_write.write(items[0]+"="+items[1]+"\n")
                
                complete_file_to_write.close()  
                messagebox.showinfo("All values are saved")

        #labels
        Label(tab1,text='''Stiffness for tension''',width=25).grid(row=0,column=0,padx=5,pady=13)
        Label(tab1,text='''Stiffness for Compression''',width=25).grid(row=0,column=2,padx=5,pady=13)
        Label(tab1,text='''Clamp on catenary wire''',width=25).grid(row=1,column=0,padx=5,pady=13)
        Label(tab1,text='''Clamp on Contact wire''',width=25).grid(row=1,column=2,padx=5,pady=13)
        Label(tab1,text='''Mass per unit length''',width=25).grid(row=2,column=0,padx=5,pady=13)

        #Entry Box
        en6 = Entry(tab1,textvariable=var1).grid(row=0,column=1,padx=5,pady=13)
        en2 = Entry(tab1,textvariable=var2).grid(row=0,column=3,padx=5,pady=13)
        en3 = Entry(tab1,textvariable=var3).grid(row=1,column=1,padx=5,pady=13)
        en4 = Entry(tab1,textvariable=var4).grid(row=1,column=3,padx=5,pady=13)
        en5 = Entry(tab1,textvariable=var5).grid(row=2,column=1,padx=5,pady=13)
        

        #button
        btn = Button(tab1,text="Simulate",command=func)
        btn.place(x=300,y=300)


    #tab2 function to generate tab2;
    def tab2func():

        def fun():
            pass

        Label(tab2,text='''Span length''',width=25).grid(row=0,column=0,padx=5,pady=13)
        splen=Entry(tab2).grid(row=0,column=1,padx=5, pady=13)

        Label(tab2,text='''Encumbrance''',width=25).grid(row=0,column=2,padx=5,pady=13)
        encum=Entry(tab2).grid(row=0,column=3,padx=5, pady=13)

        Label(tab2,text='''Length of Stitch Wire''',width=25).grid(row=1,column=0,padx=5,pady=13)
        lensw=Entry(tab2).grid(row=1,column=1,padx=5, pady=13)

        Label(tab2,text='''Maximum Presag at 
        Midspan''',width=25).grid(row=1,column=2,padx=5,pady=13)
        maxpremidspam=Entry(tab2).grid(row=1,column=3,padx=5, pady=13)

        Label(tab2,text='''Stagger of Contact Wire''',width=25).grid(row=2,column=0,padx=5,pady=13)
        staggercw=Entry(tab2).grid(row=2,column=1,padx=5, pady=13)

        Label(tab2,text='''Stagger of Catenary Wire''',width=25).grid(row=2,column=2,padx=5,pady=13)
        staggercatw=Entry(tab2).grid(row=2,column=3,padx=5, pady=13)

        btn=Button(tab2,text="Simulate",command=fun)
        btn.grid(row=8,column=2)

    #tab3 function to generate tab2;
    def tab3func():
        #Contact Wires
        def fun():
            pass

        Label(tab3,text='''Number of Contact Wires''',width=25).grid(row=0,column=0,padx=5,pady=13)
        nocw=Entry(tab3).grid(row=0,column=1,padx=5, pady=13)

        Label(tab3,text='''Tension per Wire''',width=25).grid(row=0,column=2,padx=5,pady=13)
        tension=Entry(tab3).grid(row=0,column=3,padx=5, pady=13)

        Label(tab3,text='''Mass per length Unit''',width=25).grid(row=1,column=0,padx=5,pady=13)
        massperlen=Entry(tab3).grid(row=1,column=1,padx=5, pady=13)

        Label(tab3,text='''Youngs Modules E''',width=25).grid(row=1,column=2,padx=5,pady=13)
        E=Entry(tab3).grid(row=1,column=3,padx=5, pady=13)

        Label(tab3,text='''Cross Section''',width=25).grid(row=2,column=0,padx=5,pady=13)
        crosssec=Entry(tab3).grid(row=2,column=1,padx=5, pady=13)

        btn=Button(tab3,text="Simulate",command=fun)
        btn.grid(row=8,column=2)

    #tab4 function to generate tab2;
    def tab4func():
        #Messenger Wires
        def fun():
            pass

        Label(tab4,text='''Number of Messenger Wires''',width=25).grid(row=0,column=0,padx=5,pady=13)
        nomw=Entry(tab4).grid(row=0,column=1,padx=5, pady=13)

        Label(tab4,text='''Young's Modulus E''',width=25).grid(row=0,column=2,padx=5,pady=13)
        E=Entry(tab4).grid(row=0,column=3,padx=5, pady=13)

        Label(tab4,text='''Area of Cross Section''',width=25).grid(row=1,column=0,padx=5,pady=13)
        crosssec=Entry(tab4).grid(row=1,column=1,padx=5, pady=13)

        Label(tab4,text='''Tension''',width=25).grid(row=1,column=2,padx=5,pady=13)
        tension=Entry(tab4).grid(row=1,column=3,padx=5, pady=13)

        Label(tab4,text='''Mass per length unit''',width=25).grid(row=2,column=0,padx=5,pady=13)
        massperlen=Entry(tab4).grid(row=2,column=1,padx=5, pady=13)

        btn=Button(tab4,text="Simulate",command=fun)
        btn.grid(row=8,column=2)


    tab1func()
    tab2func()
    tab3func()
    tab4func()
btn = Button(Master,
             text ="Go",
             command = newWindow)
btn.pack(pady = 10)
# mainloop, runs infinitely
mainloop()