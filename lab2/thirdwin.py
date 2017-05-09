from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import fourthwin


class ThirdWin(Tk):

    def __init__(self):
        super().__init__()
        self.parse()
        self.initFonts()
        self.initUI()
        self.initSets()

    def parse(self):
        self.set_women, self.set_men = set(), set()
        with open(r"women.txt", "r") as f:
            for i in f.read().split():
                self.set_women.add(i)
        with open(r"men.txt", "r") as f:
            for i in f.read().split():
                self.set_men.add(i)


    def initFonts(self):
        """Ініціалізація шрифтів, кольорів"""
        self.color = "#8bb2d3"
        self.font_H1 = Font(self, name="font_H1", family="Helvetica", size=18)
        self.font_p = Font(self, name="font_p", family="Helvetica", size=14)
        self.font_button = Font(self, name="font_button", family="Helvetica", size=10)
        self.font_set = Font(self, name="font_set", family="Helvetica", size=8)

    def initUI(self):
        """Ініціалізація графічного інтерфейсу"""
        self.title("Бінарні відношення")
        self.center()
        self["bg"] = self.color

        # Frame з множинами А і В

        self.frame_sets = Frame(self, bd=5, bg=self.color)
        self.lbl_setA = Label(self.frame_sets, text="Множина А: ", bg=self.color, font="font_button")
        self.lbox_setA = Listbox(self.frame_sets, font="font_button")
        self.lbl_setB = Label(self.frame_sets, text="Множина В: ", bg=self.color, font="font_button")
        self.lbox_setB = Listbox(self.frame_sets, font="font_button")
        self.but = Button(self, text="Побудувати матриці", command=self.make)
        self.but_next = Button(self, text="Далі", command=self.next)
        self.lbl_S = Label(self.frame_sets, text="Відношення S", bg=self.color)
        self.lbl_R = Label(self.frame_sets, text="Відношення R", bg=self.color)

        self.txt_S = Text(self.frame_sets, height=14, width=100, bd=4)
        self.txt_R = Text(self.frame_sets, height=14, width=100, bd=4)

        # grid

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.frame_sets.grid(row=0, column=0, rowspan=2)
        self.lbl_setA.grid(row=0, column=0, sticky="sw")
        self.lbox_setA.grid(row=1, column=0, rowspan=2)
        self.lbl_setB.grid(row=3, column=0, sticky="sw")
        self.lbox_setB.grid(row=4, column=0, rowspan=2)
        self.lbl_S.grid(row=0, column=1)
        self.txt_S.grid(row=1, column=1, rowspan=2)
        self.lbl_R.grid(row=3, column=1)
        self.txt_R.grid(row=4, column=1, rowspan=2)
        self.but.grid()
        self.but_next.grid()

        self.protocol("WM_DELETE_WINDOW", self.messagequit)

    def initSets(self):
        ThirdWin.setA, ThirdWin.setB = set(), set()
        self.lbox_setA.delete(0, END)
        self.lbox_setB.delete(0, END)
        with open(r"setA.txt", "r") as f:
            for i in f.read().split():
                self.lbox_setA.insert(END, i)
                ThirdWin.setA.add(i)
        with open(r"setB.txt", "r") as f:
            for i in f.read().split():
                self.lbox_setB.insert(END, i)
                ThirdWin.setB.add(i)
        ThirdWin.UNI = set()
        for i in ThirdWin.setA:
            for j in ThirdWin.setB:
                ThirdWin.UNI.add((i,j))

    def center(self):
        """Метод центрування вікна"""
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.wm_geometry("+%d+%d" % (x - 50, y - 100))

    def make(self):
        """Метод створення бінарних відношень за власним алгоритмом"""
        self.txt_R.delete(0.0, END)
        self.txt_S.delete(0.0, END)
        setA, setB = list(ThirdWin.setA.copy()), list(ThirdWin.setB.copy())
        self.S, self.R = set(), set()

        setB_no_women = list(filter(lambda x: x in self.set_men, setB))
        setA_no_men = list(filter(lambda x: x in self.set_women, setA))

        self.R = set(zip(setA_no_men, setB_no_women))
        self.S = set(zip(setA_no_men, setB[::-1]))
        self.S = set(filter(lambda x: x not in self.R, self.S))
        self.S = set(filter(lambda x: x[0] != x[1], self.S))
        self.S = set(filter(lambda x: (x[0], x[1]) != (x[1], x[0]), self.S))

        self.matrix(self.S, self.txt_S, r"S.txt")
        self.matrix(self.R, self.txt_R, r"R.txt")

    # self.S и self.R - отpимані бінарні множини

    def matrix(self, rel, text, file):
        """Відображає матриці створених відношень"""

        # Створення матриці, заповненої нулями
        set1 = list(ThirdWin.setA)
        set2 = list(ThirdWin.setB)
        n = len(set1)
        m = len(set2)
        list_ = [0] * n
        for i in range(n):
            list_[i] = [0] * m

        # Розставляємо "одинички"

        count_i = 0
        for i in set1:
            count_j = 0
            for j in set2:
                if (i, j) in rel:
                    list_[count_i][count_j] = 1
                count_j += 1
            count_i += 1

        # Додаємо імена в матрицю

        count = 0
        for i in set1:
            list_[count].insert(0, i)
            count += 1
        list_.insert(0, set2)
        list_[0].insert(0, " " * 10)

        # Виводимо в Text

        for i in list_:
            if list_.index(i) == 0:
                for j in i:
                    text.insert(END, "{:<10}".format(j))
            else:
                for j in i:
                    text.insert(END, "{:^10}".format(j))
            text.insert(END, "\n")

        # Виконуємо запис до вказаного файлу

        with open(file, "w") as f:
            for i in list_:
                for j in i:
                    f.write("{:<10}".format(j))
                f.write("\n")

    def next(self):
        try:
            fourthwin.FourthWin.S = self.S
            fourthwin.FourthWin.R = self.R
            fourthwin.FourthWin.UNI = ThirdWin.UNI
        except AttributeError:
            messagebox.showerror("Помилка", "Відношення S або R не було сформоване!")
        else:
            fourth = fourthwin.FourthWin()

    def messagequit(self):
        """Метод визову messagebox для виходу з програми"""
        if messagebox.askyesno("Quit", "Завершити роботу?"):
            sys.exit()

if __name__ == "__main__":
    root = ThirdWin()
    root.mainloop()
