from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter.ttk import Combobox

class Combinatorics(Tk):
    def __init__(self):

        super().__init__()
        self.initFonts()
        self.initUI()

    def initFonts(self):
        """Ініціалізація шрифтів, кольорів"""
        self.color = "#8bb2d3"
        self.font_H1 = Font(self, name="font_H1", family="Verdana", size=18)
        self.font_p = Font(self, name="font_p", family="Verdana", size=14)
        self.font_work = Font(self, name="work", family="Verdana", size=10)

    def initUI(self):
        self.title("Комбінаторика")
        self.center()
        self["bg"] = self.color

        self.frame_top = Frame(self, bg=self.color, bd=5)
        self.lbl_input = Label(self.frame_top, text="Введіть рядок-множину:",
                               bg=self.color, font="font_p")
        self.ent_input = Entry(self.frame_top, font="font_work", width=35)
        self.btn_read = Button(self.frame_top, text="Зчитати",
                               font="font_work", command=self.input)
        self.lbl_output = Label(self.frame_top, text="Отримана множина:",
                                bg=self.color, font="font_p")
        self.ent_output = Entry(self.frame_top, font="font_work", width=45)

        self.frame_middle = Frame(self, bg=self.color, bd=5)
        self.lbl_m = Label(self.frame_middle, text="m = ",
                           font="font_work", bg=self.color)
        self.combobox = Combobox(self.frame_middle, values=[0],
                                 height=3, width=3, font="font_work")
        self.listbox = Listbox(self.frame_middle, height=10, font="font_work")

        self.btn_start = Button(self, text="Знайти підмножини",
                                font="font_work", command=self.start)

    #     grid

        self.frame_top.grid(row=0, column=0)
        self.lbl_input.grid(row=0, column=0, sticky="w")
        self.ent_input.grid(row=1, column=0)
        self.btn_read.grid(row=1, column=1)
        self.lbl_output.grid(row=2, column=0, sticky="w")
        self.ent_output.grid(row=3, column=0, columnspan=2, sticky="w")

        self.frame_middle.grid(row=1, column=0)
        self.lbl_m.grid(row=0, column=0, sticky="wn")
        self.combobox.grid(row=0, column=1, sticky="wn")
        self.listbox.grid(row=0, column=2)

        self.btn_start.grid(row=2, column=0, sticky="s")

    def start(self):
        self.listbox.delete(0, END)
        m = self.combobox.get()
        if m.isdigit():
            try:
                sorted_set = sorted(self.set)[::-1]
                sorted_set.append(None)
            except AttributeError:
                messagebox.showerror("Помилка", "Не задана множина!")
            else:
                subsets = []
                cur_set = set()
                flag = True
                while flag:
                    for j in range(0, len(sorted_set)):
                        elem = sorted_set[j]
                        if not elem:
                            flag = False
                            break
                        if elem not in cur_set:
                            cur_set -= set(sorted_set[:j])
                            cur_set.update(elem)
                            if len(cur_set) == int(m):
                                subsets.append(list(cur_set))
                            break
        else:
            messagebox.showerror("Помилка", "Оберіть кількість підмножин m!")

        result = []
        for i in subsets:
            result.append(sorted(i))
        result.sort(key= lambda x : x[::-1], reverse=True)
        for i in result:
            self.listbox.insert(END, i)

    def input(self):
        self.set = set()
        self.ent_output.delete(0, END)
        text = self.ent_input.get().split()
        for i in text:
            self.set.update(i.lower())
        power = len(self.set)
        self.ent_output.insert(0, sorted(self.set))
        self.combobox["values"] = [x for x in range(1, power+1)]

    def center(self):
        """Метод центрування вікна"""
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.wm_geometry("+%d+%d" % (x, y))

if __name__ == "__main__":
    root = Combinatorics()
    root.mainloop()