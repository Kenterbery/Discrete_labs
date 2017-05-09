from tkinter import *
import fifthwindow


class Window4(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("1000x285")
        self.title("Fourth window")

        #x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        #y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        #self.wm_geometry("+%d+%d" % (x, y))

        def start(event):
            try:
                func()
                txt_result.insert("3.3", Window4.z)
                fifthwindow.Window5.Z1 = Window4.z
            except AttributeError:
                txt_result.delete("1.0", END)
                txt_result.insert("1.0", "Аргумент не був знайдений")

        def save(event):
            with open(r"result4.txt", "w") as f:
                try:
                    f.write("Z1 : " + str(Window4.z))
                except AttributeError:
                    f.write("Результат відсутній")

        def func():
            Window4.z = set()
            with fifthwindow.Profiler() as p:
                for i in Window4.setX:
                    if i not in Window4.setY:
                        Window4.z.add(i)

        txtA = Text(self,height=4, width=200, wrap=WORD)
        txtB = Text(self,height=4, width=200, wrap=WORD)
        lbl_lbl = Label(self, text="Результат:", width=10)
        txt_result = Text(self, height=4, width=100, wrap=WORD)
        btn_res = Button(self, text="Розрахувати")
        btn_res.bind("<Button-1>", start)
        btn_save = Button(self, text="Зберегти")
        btn_save.bind("<Button-1>", save)

        try:
            txtA.insert("1.0", Window4.setX)
        except AttributeError:
            txtA.delete("1.0", END)
            txtA.insert("1.0", "Множина X: "+"Значення не знайдене")
        try:
            txtB.insert("1.0", Window4.setY)
        except AttributeError:
            txtB.delete("1.0", END)
            txtB.insert("1.0", "Множина Y: "+"Значення не знайдене")
        txt_result.insert("1.0", "Z = X \ Y    :   ")

        txtA.grid(row=0, columnspan=3)
        txtB.grid(row=1, columnspan=3)
        lbl_lbl.grid(row=3, column=0, sticky="w")
        txt_result.grid(row=5, columnspan=2)
        btn_res.grid(row=6, sticky="e")
        btn_save.grid(sticky="w")


if __name__ == "__main__":
    root = Window4()
    root.mainloop()