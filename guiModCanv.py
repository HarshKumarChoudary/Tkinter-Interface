from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import sqlite3

# -----------------------------------------------------------------------------------------------------------------------------------------
# creating main window
Master = Tk()
type_of_wire = StringVar()
Master.geometry("300x300")
labelm = Label(Master, text="Please Select the type of wire you want to use")
labelm.pack(pady=10)
values = {"AC Simple": "1",
          "AC Stitched": "2",
          "DC Simple": "3",
          }

for (text, value) in values.items():
    Radiobutton(Master, text=text, variable=type_of_wire,
                value=value).pack(fill=X, ipady=5)

# -----------------------------------------------------------------------------------------------------------------------------------------
# function when first window is called and it represents windows and tabs to collect data.


def newWindow():

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
                conn = sqlite3.connect('catenary.db')
                connn = conn.cursor()
                connn.execute("""DROP TABLE IF EXISTS Droppers""")
                connn.execute('''CREATE TABLE Droppers(
                                Title           TEXT    NOT NULL,
                                Value            INT     NOT NULL
                            )''')
                list_of_items = [['Stiffness for tension [N/m]', val1], ['Stiffness for Compression [N/m]', val2], [
                    'Clamp on catenary wire [Kg]', val3], ['Clamp on Contact wire [Kg]', val4], ['Mass per unit length [Kg/m]', val5]]
                for items in list_of_items:
                    connn.execute(
                        "INSERT INTO Droppers VALUES (?,?)", (items[0], items[1]))

                conn.commit()
                messagebox.showinfo("All values are saved")

        def func2():
            conn = sqlite3.connect('catenary.db')
            connn = conn.cursor()
            ls = []
            ls.append(['Droppers'])
            ls.append(connn.execute("SELECT * FROM Droppers").fetchall())
            ls.append(['Geometry'])
            ls.append(connn.execute("SELECT * FROM Geometry").fetchall())
            ls.append(['ContactWire'])
            ls.append(connn.execute("SELECT * FROM ContactWire").fetchall())
            ls.append(['Messengerwire'])
            ls.append(connn.execute("SELECT * FROM Messengerwire").fetchall())
            ls.append(['steadyArm'])
            ls.append(connn.execute("SELECT * FROM steadyArm").fetchall())
            if type_of_wire.get() == "2":
                ls.append(['StitchWire'])
                ls.append(connn.execute("SELECT * FROM StitchWire").fetchall())
            if type_of_wire.get() == "1":
                ls.append(['MessengerWireSupport'])
                ls.append(connn.execute(
                    "SELECT * FROM MessengerWireSupport").fetchall())

            conn.commit()
            # code to create a final interface output.
            root2 = Tk()
            t = Text(root2)
            for x in ls:
                for y in x:
                    if len(x) == 1:
                        t.insert(END, y+'\n')
                    else:
                        t.insert(END, y[0] + " " + str(y[1]) + '\n')
                t.insert(END, '\n')
            t.pack()
            root2.geometry("1000x700")
            root2.mainloop()

            Master.destroy()

        Label(tab1, text='''Stiffness for tension''', width=25).grid(
            row=0, column=0, padx=5, pady=13)
        Label(tab1, text='''Stiffness for Compression''',
              width=25).grid(row=0, column=2, padx=5, pady=13)
        Label(tab1, text='''Clamp on catenary wire''', width=25).grid(
            row=1, column=0, padx=5, pady=13)
        Label(tab1, text='''Clamp on Contact wire''', width=25).grid(
            row=1, column=2, padx=5, pady=13)
        Label(tab1, text='''Mass per unit length''', width=25).grid(
            row=2, column=0, padx=5, pady=13)

        en1 = Entry(tab1, textvariable=var1).grid(
            row=0, column=1, padx=5, pady=13)
        en2 = Entry(tab1, textvariable=var2).grid(
            row=0, column=3, padx=5, pady=13)
        en3 = Entry(tab1, textvariable=var3).grid(
            row=1, column=1, padx=5, pady=13)
        en4 = Entry(tab1, textvariable=var4).grid(
            row=1, column=3, padx=5, pady=13)
        en5 = Entry(tab1, textvariable=var5).grid(
            row=2, column=1, padx=5, pady=13)

        btn = Button(tab1, text="Save", command=func)
        btn2 = Button(tab1, text="Simulate", command=func2)
        btn.place(x=300, y=300)
        btn2.place(x=300, y=400)

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
                conn = sqlite3.connect('catenary.db')
                connn = conn.cursor()
                connn.execute("""DROP TABLE IF EXISTS Geometry""")
                connn.execute('''CREATE TABLE Geometry(
                                Title           TEXT    NOT NULL,
                                Value            INT     NOT NULL
                            )''')
                list_of_items = [['Span Length [m]', val1], ['Encumbrance [m]', val2], ['Length of Stitch Wire [m]', val3], [
                    'Maximum Presag at Midspan [mm]', val4], ['Stagger of Contact Wire [m]', val5], ['Stagger of Catenary Wire [m]', val6]]
                for items in list_of_items:
                    connn.execute(
                        "INSERT INTO Geometry VALUES (?,?)", (items[0], items[1]))
                conn.commit()
                messagebox.showinfo("All values are saved")

            # Add function to show image

            if type_of_wire.get() == '1':
                top = Toplevel()
                top.title("AC – Simple - overhead contact line model")
                myImg = ImageTk.PhotoImage(Image.open("ACSimplePNG.png"))
                mylabel = Label(top, image=myImg)
                mylabel.image = myImg

                tableList = [("Variable", "Property", "Value", "Unit"), ("a", "Span length ", var1.get(), " meters"),
                             ("b", "Encumbrance ", var2.get(), " meters"),
                             ("c", "Maximum Presag at Midspan ", var4.get(), " millimeters")]
                for i in range(len(tableList)):
                    for j in range(len(tableList[0])):
                        eTable = Entry(top, width=32, foreground="blue",
                                       font=('Arial', 15, 'bold'))
                        eTable.grid(row=i, column=j)
                        eTable.insert(0, tableList[i][j])

                mylabel.grid(row=4, column=1, columnspan=2, sticky=N+S)
            if type_of_wire.get() == '2':
                top = Toplevel()
                top.title("AC - Stitched catenary overhead contact line model")
                myImg = ImageTk.PhotoImage(Image.open("ACStitchedPNG.png"))
                mylabel = Label(top, image=myImg)
                mylabel.image = myImg

                tableList = [("Variable", "Property", "Value", "Unit"), ("a", "Span length ", var1.get(), " meters"),
                             ("b", "Encumbrance ", var2.get(), " meters"),
                             ("c", "Length of stitch wire", str(int(var3.get())/2), " meters")]
                for i in range(len(tableList)):
                    for j in range(len(tableList[0])):
                        eTable = Entry(top, width=32, foreground="blue",
                                       font=('Arial', 15, 'bold'))
                        eTable.grid(row=i, column=j)
                        eTable.insert(0, tableList[i][j])

                mylabel.grid(row=4, column=1, columnspan=2, sticky=N+S)
            if type_of_wire.get() == '3':
                top = Toplevel()
                top.title("DC – simple catenary overhead contact line model")
                myImg = ImageTk.PhotoImage(Image.open("DCSimplePNG.png"))
                mylabel = Label(top, image=myImg)
                mylabel.image = myImg

                tableList = [("Variable", "Property", "Value", "Unit"), ("a", "Span length ", var1.get(), " meters"),
                             ("b", "Encumbrance ", var2.get(), " meters"),
                             ("c", "Maximum Presag at Midspan ", var4.get(), " millimeters")]
                for i in range(len(tableList)):
                    for j in range(len(tableList[0])):
                        eTable = Entry(top, width=32, foreground="blue",
                                       font=('Arial', 15, 'bold'))
                        eTable.grid(row=i, column=j)
                        eTable.insert(0, tableList[i][j])

                mylabel.grid(row=4, column=1, columnspan=2, sticky=N+S)

        Label(tab2, text='''Span length''', width=25).grid(
            row=0, column=0, padx=5, pady=13)
        Label(tab2, text='''Encumbrance''', width=25).grid(
            row=0, column=2, padx=5, pady=13)
        Label(tab2, text='''Length of Stitch Wire''', width=25).grid(
            row=1, column=0, padx=5, pady=13)
        Label(tab2, text='''Maximum Presag at Midspan''',
              width=25).grid(row=1, column=2, padx=5, pady=13)
        Label(tab2, text='''Stagger of Contact Wire''', width=25).grid(
            row=2, column=0, padx=5, pady=13)
        Label(tab2, text='''Stagger of Catenary Wire''',
              width=25).grid(row=2, column=2, padx=5, pady=13)

        en1 = Entry(tab2, textvariable=var1).grid(
            row=0, column=1, padx=5, pady=13)
        en2 = Entry(tab2, textvariable=var2).grid(
            row=0, column=3, padx=5, pady=13)
        en3 = Entry(tab2, textvariable=var3).grid(
            row=1, column=1, padx=5, pady=13)
        en4 = Entry(tab2, textvariable=var4).grid(
            row=1, column=3, padx=5, pady=13)
        en5 = Entry(tab2, textvariable=var5).grid(
            row=2, column=1, padx=5, pady=13)
        en5 = Entry(tab2, textvariable=var6).grid(
            row=2, column=3, padx=5, pady=13)

        btn = Button(tab2, text="Save", command=func)
        btn.place(x=300, y=300)

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
                conn = sqlite3.connect('catenary.db')
                connn = conn.cursor()
                connn.execute("""DROP TABLE IF EXISTS ContactWire""")
                connn.execute('''CREATE TABLE ContactWire(
                                Title           TEXT    NOT NULL,
                                Value            INT     NOT NULL
                            )''')
                list_of_items = [['Number of Contact Wires', val1], ['Tension per Wire [N]', val2], [
                    'Mass per length Unit [kg/m]', val3], ['Youngs Modules [kN/mm^2]', val4], ['Cross Section [mm^2]', val5]]
                for items in list_of_items:
                    connn.execute(
                        "INSERT INTO ContactWire VALUES (?,?)", (items[0], items[1]))
                conn.commit()
                messagebox.showinfo("All values are saved")

        Label(tab3, text='''Number of Contact Wires''', width=25).grid(
            row=0, column=0, padx=5, pady=13)
        Label(tab3, text='''Tension per Wire''', width=25).grid(
            row=0, column=2, padx=5, pady=13)
        Label(tab3, text='''Mass per length Unit''', width=25).grid(
            row=1, column=0, padx=5, pady=13)
        Label(tab3, text='''Youngs Modules E''', width=25).grid(
            row=1, column=2, padx=5, pady=13)
        Label(tab3, text='''Cross Section''', width=25).grid(
            row=2, column=0, padx=5, pady=13)

        en1 = Entry(tab3, textvariable=var1).grid(
            row=0, column=1, padx=5, pady=13)
        en2 = Entry(tab3, textvariable=var2).grid(
            row=0, column=3, padx=5, pady=13)
        en3 = Entry(tab3, textvariable=var3).grid(
            row=1, column=1, padx=5, pady=13)
        en4 = Entry(tab3, textvariable=var4).grid(
            row=1, column=3, padx=5, pady=13)
        en5 = Entry(tab3, textvariable=var5).grid(
            row=2, column=1, padx=5, pady=13)

        btn = Button(tab3, text="Save", command=fun)
        btn.place(x=300, y=300)

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
                conn = sqlite3.connect('catenary.db')
                connn = conn.cursor()
                connn.execute("""DROP TABLE IF EXISTS MessengerWire""")
                connn.execute('''CREATE TABLE MessengerWire(
                                Title           TEXT    NOT NULL,
                                Value            INT     NOT NULL
                            )''')
                list_of_items = [['Number of Messenger Wires', val1], ['Young\'s Modulus E [kN/mm^2]', val2], [
                    'Area of Cross Section [mm^2]', val3], ['Tension [N]', val4], ['Mass per length unit [Kg/m]', val5]]
                for items in list_of_items:
                    connn.execute(
                        "INSERT INTO MessengerWire VALUES (?,?)", (items[0], items[1]))
                conn.commit()
                messagebox.showinfo("All values are saved")

        Label(tab4, text='''Number of Messenger Wires''',
              width=25).grid(row=0, column=0, padx=5, pady=13)
        Label(tab4, text='''Young's Modulus E''', width=25).grid(
            row=0, column=2, padx=5, pady=13)
        Label(tab4, text='''Area of Cross Section''', width=25).grid(
            row=1, column=0, padx=5, pady=13)
        Label(tab4, text='''Tension''', width=25).grid(
            row=1, column=2, padx=5, pady=13)
        Label(tab4, text='''Mass per length unit''', width=25).grid(
            row=2, column=0, padx=5, pady=13)

        en1 = Entry(tab4, textvariable=var1).grid(
            row=0, column=1, padx=5, pady=13)
        en2 = Entry(tab4, textvariable=var2).grid(
            row=0, column=3, padx=5, pady=13)
        en3 = Entry(tab4, textvariable=var3).grid(
            row=1, column=1, padx=5, pady=13)
        en4 = Entry(tab4, textvariable=var4).grid(
            row=1, column=3, padx=5, pady=13)
        en5 = Entry(tab4, textvariable=var5).grid(
            row=2, column=1, padx=5, pady=13)

        btn = Button(tab4, text="Save", command=fun)
        btn.place(x=300, y=300)

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
                conn = sqlite3.connect('catenary.db')
                connn = conn.cursor()
                connn.execute("""DROP TABLE IF EXISTS StitchWire""")
                connn.execute('''CREATE TABLE StitchWire(
                                Title           TEXT    NOT NULL,
                                Value            INT     NOT NULL
                            )''')
                list_of_items = [['clamp to Catenary Wire [Kg]', val1], ['Young\'s Modulus E [kN/mm^2]', val2], [
                    'Area of Cross Section [mm^2]', val3], ['Tension [N]', val4], ['Mass per length unit [kg/m]', val5]]

                for items in list_of_items:
                    connn.execute(
                        "INSERT INTO StitchWire VALUES (?,?)", (items[0], items[1]))
                conn.commit()
                messagebox.showinfo("All values are saved")

        Label(tab5, text='''clamp to Catenary Wire''', width=25).grid(
            row=0, column=0, padx=5, pady=13)
        Label(tab5, text='''Young's Modulus''', width=25).grid(
            row=0, column=2, padx=5, pady=13)
        Label(tab5, text='''Area of Cross Section''', width=25).grid(
            row=1, column=0, padx=5, pady=13)
        Label(tab5, text='''Tension''', width=25).grid(
            row=1, column=2, padx=5, pady=13)
        Label(tab5, text='''Mass per length unit''', width=25).grid(
            row=2, column=0, padx=5, pady=13)

        # Entry Box
        en1 = Entry(tab5, textvariable=var1).grid(
            row=0, column=1, padx=5, pady=13)
        en2 = Entry(tab5, textvariable=var2).grid(
            row=0, column=3, padx=5, pady=13)
        en3 = Entry(tab5, textvariable=var3).grid(
            row=1, column=1, padx=5, pady=13)
        en4 = Entry(tab5, textvariable=var4).grid(
            row=1, column=3, padx=5, pady=13)
        en5 = Entry(tab5, textvariable=var5).grid(
            row=2, column=1, padx=5, pady=13)

        # button
        btn = Button(tab5, text="Save", command=func)
        btn.place(x=300, y=300)

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
                conn = sqlite3.connect('catenary.db')
                connn = conn.cursor()
                connn.execute("""DROP TABLE IF EXISTS steadyArm""")
                connn.execute('''CREATE TABLE steadyArm(
                                Title           TEXT    NOT NULL,
                                Value            INT     NOT NULL
                            )''')
                list_of_items = [['Number of Arms', val1], ['Length [m]', val2], [
                    'Mass per unit length [Kg/m]', val3], ['Mass on clamp [m]', val4]]
                for items in list_of_items:
                    connn.execute(
                        "INSERT INTO steadyArm VALUES (?,?)", (items[0], items[1]))
                conn.commit()
                messagebox.showinfo("All values are saved")

        Label(tab6, text='''Number of Arms''', width=25).grid(
            row=0, column=0, padx=5, pady=13)
        Label(tab6, text='''Length''', width=25).grid(
            row=0, column=2, padx=5, pady=13)
        Label(tab6, text='''Mass per unit length''', width=25).grid(
            row=1, column=0, padx=5, pady=13)
        Label(tab6, text='''Mass on clamp''', width=25).grid(
            row=1, column=2, padx=5, pady=13)

        en1 = Entry(tab6, textvariable=var1).grid(
            row=0, column=1, padx=5, pady=13)
        en2 = Entry(tab6, textvariable=var2).grid(
            row=0, column=3, padx=5, pady=13)
        en3 = Entry(tab6, textvariable=var3).grid(
            row=1, column=1, padx=5, pady=13)
        en4 = Entry(tab6, textvariable=var4).grid(
            row=1, column=3, padx=5, pady=13)

        btn = Button(tab6, text="Save", command=func)
        btn.place(x=300, y=300)

    def tab7func():
        var2 = StringVar()
        var1 = StringVar()

        def func():
            val2 = var2.get()
            val1 = var1.get()

            if val2 == "" or val1 == "":
                messagebox.showwarning("Some values are not entered")
            else:
                conn = sqlite3.connect('catenary.db')
                connn = conn.cursor()
                connn.execute("""DROP TABLE IF EXISTS MessengerWireSupport""")
                connn.execute('''CREATE TABLE MessengerWireSupport(
                                Title           TEXT    NOT NULL,
                                Value            INT     NOT NULL
                            )''')
                list_of_items = [['Stiffness [KN/m]', val1],
                                 ['Damping [Ns/m]', val2]]
                for items in list_of_items:
                    connn.execute(
                        "INSERT INTO MessengerWireSupport VALUES (?,?)", (items[0], items[1]))

                conn.commit()
                messagebox.showinfo("All values are saved")

        # labels
        Label(tab7, text='''Stiffness''', width=25).grid(
            row=0, column=0, padx=5, pady=13)
        Label(tab7, text='''Damping''', width=25).grid(
            row=0, column=2, padx=5, pady=13)

        en1 = Entry(tab7, textvariable=var1).grid(
            row=0, column=1, padx=5, pady=13)
        en2 = Entry(tab7, textvariable=var2).grid(
            row=0, column=3, padx=5, pady=13)

        # button
        btn = Button(tab7, text="Save", command=func)
        btn.place(x=300, y=300)

     # print(type_of_wire.get())
    root = Toplevel(Master)
    root.title("Catenary Input Interface")
    root.geometry("700x700")
    notebook = Notebook(root)
    notebook.pack(expand=1, fill="both", pady=5, padx=5)

    tab1 = Frame(notebook)
    notebook.add(tab1, text="Droppers")
    tab2 = Frame(notebook)
    notebook.add(tab2, text="Geometrical Arrangement")
    tab3 = Frame(notebook)
    notebook.add(tab3, text="Contact Wires")
    tab4 = Frame(notebook)
    notebook.add(tab4, text="Messenger Wires")

    if type_of_wire.get() == "2":
        tab5 = Frame(notebook)
        notebook.add(tab5, text="Stitch Wire")

    tab6 = Frame(notebook)
    notebook.add(tab6, text="Steady Arm")

    if type_of_wire.get() == "1":
        tab7 = Frame(notebook)
        notebook.add(tab7, text="Messenger Wire Support")

    notebook.pack(expand=1, fill="both")

    tab1func()
    tab2func()
    tab3func()
    tab4func()
    if type_of_wire.get() == "2":
        tab5func()
    tab6func()
    if type_of_wire.get() == "1":
        tab7func()


# -----------------------------------------------------------------------------------------------------------------------------------------
# the main window button which will call second window.
btn = Button(Master,
             text="Go",
             command=newWindow)
btn.pack(pady=10)
# mainloop, runs infinitely
mainloop()
