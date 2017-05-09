from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import thirdwin, fourthwin

class SecWin(Tk):

    def __init__(self):
        super().__init__()
        self.initFonts()
        self.initUI()
        self.initMenu()
        self.parse()

    def initUI(self):

      # self.geometry("500x500")
        self.title("Бінарні відношення")
        self.center()
        self["bg"] = self.color

        self.variable = IntVar()

        # Frame з початковими множинами імен

        self.frame_main = Frame(self, bd=5, bg=self.color)
        self.lbl_women = Label(self.frame_main, text="Жінки:", bg=self.color, font="font_button")
        self.lbox_women = Listbox(self.frame_main, font="font_button", selectmode=EXTENDED)
        self.lbl_men = Label(self.frame_main, text="Чоловіки: ", bg=self.color, font="font_button")
        self.lbox_men = Listbox(self.frame_main, font="font_button", selectmode=EXTENDED)

        # Frame з множинами А і В

        self.frame_sets = Frame(self, bd=5, bg=self.color)
        self.lbl_setA = Label(self.frame_sets, text="Множина А: ", bg=self.color, font="font_button")
        self.lbox_setA = Listbox(self.frame_sets, font="font_button")
        self.lbl_setB = Label(self.frame_sets, text="Множина В: ", bg=self.color, font="font_button")
        self.lbox_setB = Listbox(self.frame_sets, font="font_button")

        # Frame з радіобаттонами та кнопками

        self.frame_buttons = Frame(self, bd=5, bg="#a2c8e8")
        self.rbutton_A = Radiobutton(self.frame_buttons, text="Множина А",
                                     variable=self.variable, value=1, bg="#a2c8e8",
                                     font="font_button", bd=4)
        self.rbutton_B = Radiobutton(self.frame_buttons, text="Множина В",
                                     variable=self.variable, value=2, bg="#a2c8e8",
                                     font="font_button", bd=4)
        self.btn_copy = Button(self.frame_buttons, text="Копіювати", command=self.move, font="font_button")
        self.btn_del = Button(self.frame_buttons, text="Видалити множину", font="font_button", command=self.delete)

        # Frame з кнопками знизу

        self.frame_bottom = Frame(self, bd=5, bg="#a2c8e8")
        self.button_save = Button(self.frame_bottom, text="Зберегти", command=self.save, font="font_button", bd=3)
        self.button_read = Button(self.frame_bottom, text="Зчитати", command=self.read_, font="font_button", bd=3)

        # grid

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)

        self.frame_main.grid(row=0, column=0, rowspan=2, columnspan=3)
        self.lbl_women.grid(row=0, column=0, sticky="nw")
        self.lbox_women.grid(row=1, column=0, sticky="sw")
        self.lbl_men.grid(row=0, column=1, sticky="nw")
        self.lbox_men.grid(row=1, column=1, sticky="sw")

        self.frame_buttons.grid(row=2, column=0)
        self.rbutton_A.grid(row=0, column=0, columnspan=2, sticky="w")
        self.rbutton_B.grid(row=1, column=0, columnspan=2, sticky="w")
        self.btn_copy.grid(row=0, rowspan=2, column=2, sticky="e")
        self.btn_del.grid(row=0, column=3, rowspan=2, sticky="e")

        self.frame_sets.grid(row=4, column=0, rowspan=2)
        self.lbl_setA.grid(row=0, column=0, sticky="nw")
        self.lbox_setA.grid(row=1, column=0, sticky="sw")
        self.lbl_setB.grid(row=0, column=1, sticky="nw")
        self.lbox_setB.grid(row=1, column=1, sticky="sw")

        self.frame_bottom.grid(row=6, column=0)
        self.button_save.grid(row=0, column=0, sticky="w")
        self.button_read.grid(row=0, column=1, sticky="e")

        self.protocol("WM_DELETE_WINDOW", self.messagequit)

    def initFonts(self):
        """Ініціалізація шрифтів, кольорів"""
        self.color = "#8bb2d3"
        self.font_H1 = Font(self, name="font_H1", family="Helvetica", size=18)
        self.font_p = Font(self, name="font_p", family="Helvetica", size=14)
        self.font_button = Font(self, name="font_button", family="Helvetica", size=10)


    def parse(self):
        try:
            with open(r"women.txt", "r") as f:
                for i in f.read().split():
                    self.lbox_women.insert(END, i)
        except FileNotFoundError:
            self.lbox_women.insert(END, "Файл відсутній")
        try:
            with open(r"men.txt", "r") as f:
                for i in f.read().split():
                    self.lbox_men.insert(END, i)
        except FileNotFoundError:
            self.lbox_men.insert(END, "Файл відсутній")

    def center(self):
        """Метод центрування вікна"""
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.wm_geometry("+%d+%d" % (x-100, y-150))

    def move(self):
        """Метод, що копіює значення полів початкових лістбоксів до множинних"""
        if self.variable.get() == 1:    # Якщо вибрана множина А
            for i in self.lbox_women.curselection():
                self.lbox_setA.insert(END, self.lbox_women.get(i))
            for i in self.lbox_men.curselection():
                self.lbox_setA.insert(END, self.lbox_men.get(i))
            SecWin.setA = set(self.lbox_setA.get(0, END))
            self.lbox_setA.delete(0, END)
            for i in SecWin.setA:
                self.lbox_setA.insert(END, i)
        elif self.variable.get() == 2:   # Якщо вибрана множина В
            for i in self.lbox_women.curselection():
                self.lbox_setB.insert(END, self.lbox_women.get(i))
            for i in self.lbox_men.curselection():
                self.lbox_setB.insert(END, self.lbox_men.get(i))
            SecWin.setB = set(self.lbox_setB.get(0, END))
            self.lbox_setB.delete(0, END)
            for i in SecWin.setB:
                self.lbox_setB.insert(END, i)
        else:
            self.error()

    def delete(self):
        if self.variable.get() == 1:     # Якщо вибрана множина А
            self.lbox_setA.delete(0, END)
            SecWin.setA = set()
        elif self.variable.get() == 2:   # Якщо вибрана множина В
            SecWin.setB = set()
            self.lbox_setB.delete(0, END)
        else:
            self.error()

    def save(self):
        """Зберігає вказану множину в файл"""
        if self.variable.get() == 1:     # Якщо вибрана множина А
            with open(r"setA.txt", "w") as f:
                for i in self.lbox_setA.get(0, END):
                    f.write(i+" ")
        elif self.variable.get() == 2:   # Якщо вибрана множина В
            with open(r"setB.txt", "w") as f:
                for i in self.lbox_setB.get(0, END):
                    f.write(i+" ")
        else:
            self.error()

    def read_(self):
        """Зчитує множину з файлу"""
        if self.variable.get() == 1:     # Якщо вибрана множина А
            self.lbox_setA.delete(0, END)
            with open(r"setA.txt", "r") as f:
                for i in f.read().split():
                    self.lbox_setA.insert(END, i)
        elif self.variable.get() == 2:  # Якщо вибрана множина B
            self.lbox_setB.delete(0, END)
            with open(r"setB.txt", "r") as f:
                for i in f.read().split():
                    self.lbox_setB.insert(END, i)
        else:
            self.error()

    def initMenu(self):
        self.m = Menu(self, bg="#a2c8e8")
        self.config(menu=self.m)

        self.fm = Menu(self.m, tearoff=0)
        self.em = Menu(self.m, tearoff=0)
        self.m.add_cascade(label="Open...", menu=self.fm, font="font_button")
        self.fm.add_command(label="Window 3", command=self.window3, font="font_button")
        self.fm.add_command(label="Window 4", command=self.window4, font="font_button")
        self.m.add_cascade(label="Exit...", menu=self.em, font="font_button")
        self.em.add_command(label="Quit app", command=self.messagequit, font="font_button")

    def window3(self):
        """Метод визову третього вікна"""
        third = thirdwin.ThirdWin()
        thirdwin.ThirdWin.UNI = set()
        for i in self.lbox_setA.get(0, END):
            for j in self.lbox_setB.get(0, END):
                thirdwin.ThirdWin.UNI.add((i,j))
        self.withdraw()

    def window4(self):
        """Метод визову четвертого вікна"""
        fourth = fourthwin.FourthWin()

    def messagequit(self):
        """Метод визову messagebox для виходу з програми"""
        if messagebox.askyesno("Quit", "Завершити роботу?"):
            sys.exit()

    def error(self):
        messagebox.showerror("Помилка", "Не вибрана множина!")

if __name__ == "__main__":
    root = SecWin()
    root.mainloop()