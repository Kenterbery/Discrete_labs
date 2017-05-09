from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from random import shuffle
import sys
import secwindow, thirdwindow, fourthwindow, fifthwindow



class MainWindow(Tk):

    def __get__(self, obj, cls):
        print("Trying to access from {0} class {1}".format(obj, cls))

    def __set__(self, obj, val):
        print("Trying to set {0} for {1}".format(val, obj))

    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.geometry("425x225")
        self.title("Main window")

        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.wm_geometry("+%d+%d" % (x, y))

        def set_set(set_, power, sequence, entry):
                for i in range(0, power):
                    set_.add(sequence.pop())
                entry.insert(0, set_)

        def gen(event):
            """Генерирует множества заданной мощности"""
            ent_A.delete(0, END); ent_B.delete(0, END); ent_C.delete(0, END)
            MainWindow.setA, MainWindow.setB, MainWindow.setC = set(), set(), set()
            try:
                stack = list(MainWindow.UNI)
                shuffle(stack)
                set_set(MainWindow.setA, int(powerA.get()), stack, ent_A)
                stack = list(MainWindow.UNI)
                shuffle(stack)
                set_set(MainWindow.setB, int(powerB.get()), stack, ent_B)
                stack = list(MainWindow.UNI)
                shuffle(stack)
                set_set(MainWindow.setC, int(powerC.get()), stack, ent_C)
            except AttributeError:
                ent_A.delete(0, END)
                ent_A.insert(0, "U не була знайдена")
            secwindow.Window2.setA = MainWindow.setA
            secwindow.Window2.setB = MainWindow.setB
            secwindow.Window2.setC = MainWindow.setC
            thirdwindow.Window3.setA = MainWindow.setA
            thirdwindow.Window3.setB = MainWindow.setB
            thirdwindow.Window3.setC = MainWindow.setC
            fourthwindow.Window4.setX = MainWindow.setB
            fourthwindow.Window4.setY = MainWindow.setC
            fifthwindow.Window5.setX = MainWindow.setB
            fifthwindow.Window5.setY = MainWindow.setC



        def universal(event):
            MainWindow.UNI = set()
            MainWindow.UNI = set(range(int(univers_from.get()), int(univers_to.get())+1))
            secwindow.Window2.UNI = MainWindow.UNI
            thirdwindow.Window3.UNI = MainWindow.UNI
            fourthwindow.Window4.UNI = MainWindow.UNI

        def inp(event):
            MainWindow.setA, MainWindow.setB, MainWindow.setC = set(), set(), set()
            MainWindow.setA = {int(x) for x in ent_A.get().split()}
            MainWindow.setB = {int(x) for x in ent_B.get().split()}
            MainWindow.setC = {int(x) for x in ent_C.get().split()}
            secwindow.Window2.setA = MainWindow.setA
            secwindow.Window2.setB = MainWindow.setB
            secwindow.Window2.setC = MainWindow.setC
            thirdwindow.Window3.setA = MainWindow.setA
            thirdwindow.Window3.setB = MainWindow.setB
            thirdwindow.Window3.setC = MainWindow.setC
            fourthwindow.Window4.setX = MainWindow.setB
            fourthwindow.Window4.setY = MainWindow.setC
            fifthwindow.Window5.setX = MainWindow.setB
            fifthwindow.Window5.setY = MainWindow.setC



        def window2():
            second = secwindow.Window2()

        def window3():
            third = thirdwindow.Window3()

        def window4():
            root = fourthwindow.Window4()


        def window5():
            root = fifthwindow.Window5()
            root.mainloop()

        m = Menu(self)
        self.config(menu=m)

        fm = Menu(m, tearoff=0)
        em = Menu(m, tearoff=0)
        m.add_cascade(label="Open...", menu=fm)
        fm.add_command(label="Window 2", command=window2)
        fm.add_command(label="Window 3", command=window3)
        fm.add_command(label="Window 4", command=window4)
        fm.add_command(label="Window 5", command=window5)
        m.add_cascade(label="Exit...", menu=em)
        em.add_command(label="Quit app", command=messagequit)


        #Frame с именем и вариантом
        frame_name = Frame(self, bg="white", bd=5)
        lbl_name = Label(frame_name, text="Бабко Дмитро, ІО-63",bg="white", font="Arial 18")
        lbl_var = Label(frame_name, text="Варіант: 5", bg="white")

        #Frame - рабочая область
        frame_workspace = Frame(self, bd=5)
        #Задаем мощность
        lbl_power = Label(frame_workspace, text="Потужність: ")
        powerA = ttk.Combobox(frame_workspace, values=[x for x in range(0,256)], height=6, width=5)
        powerB = ttk.Combobox(frame_workspace, values=[x for x in range(0, 256)], height=6, width=5)
        powerC = ttk.Combobox(frame_workspace, values=[x for x in range(0, 256)], height=6, width=5)
        powerA.set(0); powerB.set(0); powerC.set(0)
        #Entry для множеств
        ent_A = Entry(frame_workspace, bd=3)
        ent_B = Entry(frame_workspace, bd=3)
        ent_C = Entry(frame_workspace, bd=3)

        btn_gen = Button(frame_workspace, text="Генерувати", height=5)
        btn_gen.bind("<Button-1>",gen)

        lbl_univers_from = Label(frame_workspace, text="U від: ")
        lbl_univers_to = Label(frame_workspace, text="до: ")
        univers_from = ttk.Combobox(frame_workspace, values=[x for x in range(-255, 256)], height=6, width=5)
        univers_to = ttk.Combobox(frame_workspace, values=[x for x in range(-255, 256)], height=6, width=5)
        univers_from.set(-255); univers_to.set(255)

        btn_univers = Button(frame_workspace, text="Задати U")
        btn_univers.bind("<Button-1>", universal)

        btn_read = Button(frame_workspace, text="Зчитати множини")
        btn_read.bind("<Button-1>", inp)


        frame_name.grid(sticky="nw")
        lbl_name.grid(row=0, column=0, sticky="nw")
        lbl_var.grid(row=1, column=0, sticky="sw")

        frame_workspace.grid()
        lbl_power.grid(row=0, column=0, sticky="w")
        powerA.grid(row=0, column=1)
        powerB.grid(row=0, column=2)
        powerC.grid(row=0, column=3)
        ent_A.grid(row=1, columnspan=4, sticky="w")
        ent_B.grid(row=2, columnspan=4, sticky="w")
        ent_C.grid(row=3, columnspan=4, sticky="w")
        btn_gen.grid(row=1,rowspan=3, column=4)
        lbl_univers_from.grid(row=4, column=0, sticky="e")
        univers_from.grid(row=4, column=1)
        lbl_univers_to.grid(row=4, column=2)
        univers_to.grid(row=4, column=3)
        btn_univers.grid(row=4, column=4)
        btn_read.grid()

def messagequit():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
       sys.exit()


if __name__ == "__main__":
    root = MainWindow()
    root.protocol("WM_DELETE_WINDOW", messagequit)
    root.mainloop()