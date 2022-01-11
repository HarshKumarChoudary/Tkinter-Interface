from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os

# -----------------------------------------------------------------------------------------------------------------------------------------
#creating main window
Master = Tk()
type_of_wire = StringVar()
Master.geometry("300x300")
labelm = Label(Master, text ="Please Select the type of wire you want to use")
labelm.pack(pady = 10)
values = {"AC Simple" : "1",
          "AC Stitched" : "2",
          "DC wire" : "3",
          }

for (text, value) in values.items():
    Radiobutton(Master, text = text, variable = type_of_wire,
                value = value).pack(fill = X, ipady = 5)

# -----------------------------------------------------------------------------------------------------------------------------------------
# function when first window is called and it represents windows and tabs to collect data.
def newWindow():
    
    # print(type_of_wire.get())
    root=Toplevel(Master)
    root.title("Catenary Input Interface")
    root.geometry("700x700")
    notebook=Notebook(root)
    notebook.pack(expand=1,fill="both",pady=5,padx=5)

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
    notebook.add(tab6,text="Steady Arm")
    tab7=Frame(notebook)
    notebook.add(tab7,text="Messenger Wire Support")

    notebook.pack(expand=1,fill="both")

    def tab1func():
        var2 = StringVar()
        var3 = StringVar()
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
            Master.destroy()

        Label(tab1,text='''Stiffness for tension''',width=25).grid(row=0,column=0,padx=5,pady=13)
        Label(tab1,text='''Stiffness for Compression''',width=25).grid(row=0,column=2,padx=5,pady=13)
        Label(tab1,text='''Clamp on catenary wire''',width=25).grid(row=1,column=0,padx=5,pady=13)
        Label(tab1,text='''Clamp on Contact wire''',width=25).grid(row=1,column=2,padx=5,pady=13)
        Label(tab1,text='''Mass per unit length''',width=25).grid(row=2,column=0,padx=5,pady=13)

        en1 = Entry(tab1,textvariable=var1).grid(row=0,column=1,padx=5,pady=13)
        en2 = Entry(tab1,textvariable=var2).grid(row=0,column=3,padx=5,pady=13)
        en3 = Entry(tab1,textvariable=var3).grid(row=1,column=1,padx=5,pady=13)
        en4 = Entry(tab1,textvariable=var4).grid(row=1,column=3,padx=5,pady=13)
        en5 = Entry(tab1,textvariable=var5).grid(row=2,column=1,padx=5,pady=13)
    
        btn = Button(tab1,text="Save",command=func)       
        btn2 = Button(tab1,text="Simulate",command=Master.destroy)
        btn.place(x=300,y=300)
        btn2.place(x=300,y=400)


    def tab2func():

        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = StringVar()
        var1 = StringVar()
        var6 = StringVar()
        def func():

            val2 = var2.get()
            val3 = var3.get()
            val4 = var4.get()
            val5 = var5.get()
            val1 = var1.get()
            val6 = var6.get()
            if val3 == "" or val2 == "" or val5 == "" or val4 == "" or val1 == "" or val6 == "":
                messagebox.showwarning("Some values are not entered")
            else:
                complete_file_to_write = open("Inputs_Geometry.txt","w+")
                list_of_items = [['Span Length',val1],['Encumbrance',val2],['Length of Stitch Wire',val3],['Maximum Presag at Midspan',val4],['Stagger of Contact Wire',val5],['Stagger of Catenary Wire',val6]]
                for items in list_of_items :
                    complete_file_to_write.write(items[0]+"="+items[1]+"\n")
                
                complete_file_to_write.close()  
                messagebox.showinfo("All values are saved")

        Label(tab2,text='''Span length''',width=25).grid(row=0,column=0,padx=5,pady=13)
        Label(tab2,text='''Encumbrance''',width=25).grid(row=0,column=2,padx=5,pady=13)
        Label(tab2,text='''Length of Stitch Wire''',width=25).grid(row=1,column=0,padx=5,pady=13)
        Label(tab2,text='''Maximum Presag at Midspan''',width=25).grid(row=1,column=2,padx=5,pady=13)
        Label(tab2,text='''Stagger of Contact Wire''',width=25).grid(row=2,column=0,padx=5,pady=13)
        Label(tab2,text='''Stagger of Catenary Wire''',width=25).grid(row=2,column=2,padx=5,pady=13)

        en1 = Entry(tab2,textvariable=var1).grid(row=0,column=1,padx=5,pady=13)
        en2 = Entry(tab2,textvariable=var2).grid(row=0,column=3,padx=5,pady=13)
        en3 = Entry(tab2,textvariable=var3).grid(row=1,column=1,padx=5,pady=13)
        en4 = Entry(tab2,textvariable=var4).grid(row=1,column=3,padx=5,pady=13)
        en5 = Entry(tab2,textvariable=var5).grid(row=2,column=1,padx=5,pady=13)
        en5 = Entry(tab2,textvariable=var6).grid(row=2,column=3,padx=5,pady=13)

        btn=Button(tab2,text="Save",command=func)
        btn.place(x=300,y=300)

    def tab3func():
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = StringVar()
        var1 = StringVar()

        def fun():

            val2 = var2.get()
            val3 = var3.get()
            val4 = var4.get()
            val5 = var5.get()
            val1 = var1.get()
            if val3 == "" or val2 == "" or val5 == "" or val4 == "" or val1 == "":
                messagebox.showwarning("Some values are not entered")
            else:
                complete_file_to_write = open("Inputs_ContactWire.txt","w+")
                list_of_items = [['Number of Contact Wires',val1],['Tension per Wire',val2],['Mass per length Unit',val3],['Youngs Modules',val4],['Cross Section',val5]]
                for items in list_of_items :
                    complete_file_to_write.write(items[0]+"="+items[1]+"\n")
                
                complete_file_to_write.close()  
                messagebox.showinfo("All values are saved")

        Label(tab3,text='''Number of Contact Wires''',width=25).grid(row=0,column=0,padx=5,pady=13)
        Label(tab3,text='''Tension per Wire''',width=25).grid(row=0,column=2,padx=5,pady=13)
        Label(tab3,text='''Mass per length Unit''',width=25).grid(row=1,column=0,padx=5,pady=13)
        Label(tab3,text='''Youngs Modules E''',width=25).grid(row=1,column=2,padx=5,pady=13)
        Label(tab3,text='''Cross Section''',width=25).grid(row=2,column=0,padx=5,pady=13)

        en1 = Entry(tab3,textvariable=var1).grid(row=0,column=1,padx=5,pady=13)
        en2 = Entry(tab3,textvariable=var2).grid(row=0,column=3,padx=5,pady=13)
        en3 = Entry(tab3,textvariable=var3).grid(row=1,column=1,padx=5,pady=13)
        en4 = Entry(tab3,textvariable=var4).grid(row=1,column=3,padx=5,pady=13)
        en5 = Entry(tab3,textvariable=var5).grid(row=2,column=1,padx=5,pady=13)

        btn=Button(tab3,text="Save",command=fun)
        btn.place(x = 300,y=300)

    def tab4func():
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = StringVar()
        var1 = StringVar()

        def fun():

            val2 = var2.get()
            val3 = var3.get()
            val4 = var4.get()
            val5 = var5.get()
            val1 = var1.get()
            if val3 == "" or val2 == "" or val5 == "" or val4 == "" or val1 == "":
                messagebox.showwarning("Some values are not entered")
            else:
                complete_file_to_write = open("Inputs_Messengerwire.txt","w+")
                list_of_items = [['Number of Messenger Wires',val1],['Young\'s Modulus E',val2],['Area of Cross Section',val3],['Tension',val4],['Mass per length unit',val5]]
                for items in list_of_items :
                    complete_file_to_write.write(items[0]+"="+items[1]+"\n")
                
                complete_file_to_write.close()  
                messagebox.showinfo("All values are saved")

        Label(tab4,text='''Number of Messenger Wires''',width=25).grid(row=0,column=0,padx=5,pady=13)
        Label(tab4,text='''Young's Modulus E''',width=25).grid(row=0,column=2,padx=5,pady=13)
        Label(tab4,text='''Area of Cross Section''',width=25).grid(row=1,column=0,padx=5,pady=13)
        Label(tab4,text='''Tension''',width=25).grid(row=1,column=2,padx=5,pady=13)
        Label(tab4,text='''Mass per length unit''',width=25).grid(row=2,column=0,padx=5,pady=13)

        en1 = Entry(tab4,textvariable=var1).grid(row=0,column=1,padx=5,pady=13)
        en2 = Entry(tab4,textvariable=var2).grid(row=0,column=3,padx=5,pady=13)
        en3 = Entry(tab4,textvariable=var3).grid(row=1,column=1,padx=5,pady=13)
        en4 = Entry(tab4,textvariable=var4).grid(row=1,column=3,padx=5,pady=13)
        en5 = Entry(tab4,textvariable=var5).grid(row=2,column=1,padx=5,pady=13)

        btn=Button(tab4,text="Save",command=fun)
        btn.place(x = 300,y=300)
    
    def tab5func():
        var2 = StringVar()
        var3 = StringVar()
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
                complete_file_to_write = open("Inputs_StitchWire.txt","w+")
                list_of_items = [['clamp to Catenary Wire',val1],['Young\'s Modulus E',val2],['Area of Cross Section',val3],['Tension',val4],['Mass per length unit',val5]]
                for items in list_of_items :
                    complete_file_to_write.write(items[0]+"="+items[1]+"\n")
                
                complete_file_to_write.close()  
                messagebox.showinfo("All values are saved")

        Label(tab5,text='''clamp to Catenary Wire''',width=25).grid(row=0,column=0,padx=5,pady=13)
        Label(tab5,text='''Young's Modulus''',width=25).grid(row=0,column=2,padx=5,pady=13)
        Label(tab5,text='''Area of Cross Section''',width=25).grid(row=1,column=0,padx=5,pady=13)
        Label(tab5,text='''Tension''',width=25).grid(row=1,column=2,padx=5,pady=13)
        Label(tab5,text='''Mass per length unit''',width=25).grid(row=2,column=0,padx=5,pady=13)

        #Entry Box
        en1 = Entry(tab5,textvariable=var1).grid(row=0,column=1,padx=5,pady=13)
        en2 = Entry(tab5,textvariable=var2).grid(row=0,column=3,padx=5,pady=13)
        en3 = Entry(tab5,textvariable=var3).grid(row=1,column=1,padx=5,pady=13)
        en4 = Entry(tab5,textvariable=var4).grid(row=1,column=3,padx=5,pady=13)
        en5 = Entry(tab5,textvariable=var5).grid(row=2,column=1,padx=5,pady=13)
        

        #button
        btn = Button(tab5,text="Save",command=func)
        btn.place(x=300,y=300)
    
    def tab6func():
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var1 = StringVar()

        def func():
            val2 = var2.get()
            val3 = var3.get()
            val4 = var4.get()
            val1 = var1.get()
            if val3 == "" or val2 == "" or val4 == "" or val1 == "":
                messagebox.showwarning("Some values are not entered")
            else:
                complete_file_to_write = open("Inputs_SteadyArm.txt","w+")
                list_of_items = [['Number of Arms',val1],['Length',val2],['Mass per unit length',val3],['Mass on clamp',val4]]
                for items in list_of_items :
                    complete_file_to_write.write(items[0]+"="+items[1]+"\n")
                
                complete_file_to_write.close()  
                messagebox.showinfo("All values are saved")

        Label(tab6,text='''Number of Arms''',width=25).grid(row=0,column=0,padx=5,pady=13)
        Label(tab6,text='''Length''',width=25).grid(row=0,column=2,padx=5,pady=13)
        Label(tab6,text='''Mass per unit length''',width=25).grid(row=1,column=0,padx=5,pady=13)
        Label(tab6,text='''Mass on clamp''',width=25).grid(row=1,column=2,padx=5,pady=13)
        
        en1 = Entry(tab6,textvariable=var1).grid(row=0,column=1,padx=5,pady=13)
        en2 = Entry(tab6,textvariable=var2).grid(row=0,column=3,padx=5,pady=13)
        en3 = Entry(tab6,textvariable=var3).grid(row=1,column=1,padx=5,pady=13)
        en4 = Entry(tab6,textvariable=var4).grid(row=1,column=3,padx=5,pady=13)
        
        btn = Button(tab6,text="Save",command=func)
        btn.place(x=300,y=300)

    def tab7func():
        var2 = StringVar()
        var1 = StringVar()

        def func():
            val2 = var2.get()
            val1 = var1.get()

            if val2 == "" or val1 == "":
                messagebox.showwarning("Some values are not entered")
            else:
                complete_file_to_write = open("Inputs_MessengerWireSupport.txt","w+")
                list_of_items = [['Stiffness',val1],['Damping',val2]]
                for items in list_of_items :
                    complete_file_to_write.write(items[0]+"="+items[1]+"\n")
                
                complete_file_to_write.close()  
                messagebox.showinfo("All values are saved")

        #labels
        Label(tab7,text='''Stiffness''',width=25).grid(row=0,column=0,padx=5,pady=13)
        Label(tab7,text='''Damping''',width=25).grid(row=0,column=2,padx=5,pady=13)
      
        en1 = Entry(tab7,textvariable=var1).grid(row=0,column=1,padx=5,pady=13)
        en2 = Entry(tab7,textvariable=var2).grid(row=0,column=3,padx=5,pady=13)
        

        #button
        btn = Button(tab7,text="Save",command=func)
        btn.place(x=300,y=300)
    
    tab1func()
    tab2func()
    tab3func()
    tab4func()
    tab5func()
    tab6func()
    tab7func()
    
# -----------------------------------------------------------------------------------------------------------------------------------------
#the main window button which will call second window.
btn = Button(Master,
             text ="Go",
             command = newWindow)
btn.pack(pady = 10)
# mainloop, runs infinitely
mainloop()