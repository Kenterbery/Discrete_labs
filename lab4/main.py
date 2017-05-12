from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.initFonts()
        self.initUI()

    def initFonts(self):
        """Ініціалізація шрифтів, кольорів"""
        self.color = "#8bb2d3"
        self.font_H1 = Font(self, name="font_H1", family="Verdana", size=18)
        self.font_p = Font(self, name="font_p", family="Verdana", size=14)
        self.font_button = Font(self, name="font_button", family="Verdana", size=10)

    def initUI(self):
        self.title("Розфарбування графів")
        self.center()
        self["bg"] = self.color

        # Фрейм з імʼям

        self.frame_name = Frame(self, bg="#8bb2d3", bd=5)
        self.lbl_name = Label(self.frame_name, text="Бабко Дмитро, ІО-63", bg="#8bb2d3", font="font_H1")
        self.lbl_var = Label(self.frame_name, text="Варіант: 5", bg="#8bb2d3", font="font_p")
        self.btn_start = Button(self, text="Розпочати роботу", command=self.nextwin, underline="0", bg="silver",
                                font="font_button")

        # grid

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.frame_name.grid(sticky="nwes")
        self.lbl_name.grid(row=0, column=0, sticky="nwe")
        self.lbl_var.grid(row=1, column=0, sticky="swe")
        self.btn_start.grid(row=2, column=0, sticky="nswe")

        self.protocol("WM_DELETE_WINDOW", self.messagequit)

    def nextwin(self):
        # second = workspace.Window2()
        pass

    def messagequit(self):
        """Метод визову messagebox для виходу з програми"""
        if messagebox.askyesno("Quit", "Завершити роботу?"):
            sys.exit()

    def center(self):
        """Метод центрування вікна"""
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.wm_geometry("+%d+%d" % (x, y))


if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()
