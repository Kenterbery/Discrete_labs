from tkinter import *
import mymain as MM
import fifthwindow



class Window2(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("1000x350")
        self.title("Second window")

        #x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        #y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        #self.wm_geometry("+%d+%d" % (x, y))

        def start(event):
            try:
                Window2.d = ((Window2.setA | ((Window2.UNI - Window2.setA) & Window2.setB)) ^
                 (Window2.setC | (Window2.setC & Window2.setB)))
                txt_result.insert("3.3", Window2.d)
                fifthwindow.Window5.D1 = Window2.d
            except AttributeError:
                txt_result.delete("1.0", END)
                txt_result.insert("1.0", "Аргумент не був знайдений")

        def save(event):
            with open(r"result2.txt", "w") as f:
                try:
                    f.write("D1 : " + str(Window2.d))
                except AttributeError:
                    f.write("Результат відсутній")
        print(Window2.setA, Window2.setB)
        txtA = Text(self, height=4, width=200, wrap=WORD)
        txtB = Text(self, height=4, width=200, wrap=WORD)
        txtC = Text(self, height=4, width=200, wrap=WORD)
        lbl_lbl = Label(self, text="Результат:", width=10)
        txt_result = Text(self, height=4, width=100, wrap=WORD)
        btn_res = Button(self, text="Розрахувати")
        btn_res.bind("<Button-1>", start)
        btn_save = Button(self, text="Зберегти")
        btn_save.bind("<Button-1>", save)

        try:
            txtA.insert("1.0", Window2.setA)
        except AttributeError:
            txtA.delete("1.0", END)
            txtA.insert("1.0", "Множина А: "+"Значення не знайдене")
        try:
            txtB.insert("1.0", Window2.setB)
        except AttributeError:
            txtB.delete("1.0", END)
            txtB.insert("1.0", "Множина B: "+"Значення не знайдене")
        try:
            txtC.insert("1.0", Window2.setC)
        except AttributeError:
            txtC.delete("1.0", END)
            txtC.insert("1.0", "Множина А: "+"Значення не знайдене")
        txt_result.insert("1.0", "D1 = (Av(¬A^B))Δ(Cv(C^B))       :")

        txtA.grid(row=0, columnspan=3)
        txtB.grid(row=1, columnspan=3)
        txtC.grid(row=2, columnspan=3)
        lbl_lbl.grid(row=3, column=0, sticky="w")
        txt_result.grid(row=5, columnspan=2)
        btn_res.grid(row=6, sticky="e")
        btn_save.grid(sticky="w")


if __name__=="__main__":
    root = Window2()
    root.mainloop()



