from tkinter import *
import time


class Profiler(object):
    time=[]
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        Profiler.time.append("Elapsed time: {:.3f} nanosec".format((time.time() - self._startTime)*(10**9)))

class Window5(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("715x400")
        self.title("Fifth window")

        def read_(event):
            with open(r"result2.txt", "r") as f:
                text_d1.delete(0.0, END)
                text_d1.insert("0.0", f.read())
            with open(r"result3.txt", "r") as f:
                text_d2.delete(0.0, END)
                text_d2.insert("0.0", f.read())
            with open(r"result4.txt", "r") as f:
                text_z1.delete(0.0, END)
                text_z1.insert("0.0", f.read())

        def standart(event):
            text_z2.delete(0.0, END)
            try:
                with Profiler() as p:
                    Window5.z = Window5.setX - Window5.setY
                lbl_time_z2.config(text="Z2: " + Profiler.time[-1])
                lbl_time_z1.config(text="Z1: " + Profiler.time[-2])
                text_z2.insert("0.0", "Z2 : "+str(Window5.z))
            except AttributeError:
                text_z2.insert("0.0", "Значення не було знайдено")
            except IndexError:
                lbl_time_z1.config(text="Один з часів не був зафіксований")

        def comp(event):
            try:
                if Window5.D1 == Window5.D2:
                    lbl_d1vd2.config(text="D1 дорівнює D2")
                else:
                    lbl_d1vd2.config(text="D1 не дорівнює D2")
                if Window5.Z1 == Window5.z:
                    lbl_z1vz2.config(text="Z1 дорівнює Z2")
                else:
                    lbl_z1vz2.config(text="Z1 не дорівнює Z2")
            except AttributeError:
                lbl_d1vd2.config(text="Результат не було знайдено")
        lbl_results = Label(self, text="Результати: ")
        text_d1 = Text(self, bd=4, height=4, width=100)
        text_d2 = Text(self, bd=4, height=4, width=100)
        text_z1 = Text(self, bd=4, height=4, width=100)
        text_z2 = Text(self, bd=4, height=4, width=100)

        btn_read = Button(self, text="Зчитати")
        btn_read.bind("<Button-1>", read_)

        btn_z2 = Button(self, text="Розрахувати Z")
        btn_z2.bind("<Button-1>", standart)

        lbl_d1vd2 = Label(self)
        lbl_z1vz2 = Label(self)

        btn_comp = Button(self, text="Порівняти")
        btn_comp.bind("<Button-1>", comp)

        lbl_time_z1 = Label(self)
        lbl_time_z2 = Label(self)

        lbl_results.grid(row=0, column=0, sticky="w")
        text_d1.grid(row=1, column=0, columnspan=5, sticky="w")
        text_d2.grid(row=2, column=0, columnspan=5, sticky="w")
        text_z1.grid(row=3, column=0, columnspan=5, sticky="w")
        text_z2.grid(row=4, column=0, columnspan=5, sticky="w")
        btn_z2.grid(row=5, rowspan=2, column=0)
        btn_read.grid(row=5, rowspan=2, column=1)
        lbl_d1vd2.grid(row=7, column=0, columnspan=4,sticky="w")
        lbl_z1vz2.grid(row=8, column=0, columnspan=4, sticky="w")
        btn_comp.grid(row=9, column=0, sticky="w")
        lbl_time_z1.grid(row=7, column=4, sticky="w")
        lbl_time_z2.grid(row=8, column=4, sticky="w")

if __name__ == "__main__":
    root = Window5()
    root.mainloop()