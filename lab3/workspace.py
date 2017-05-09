from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import networkx as nx
import matplotlib.pyplot as plt

class Window2(Tk):
    def __init__(self):
        super().__init__()
        self.initFonts()

        self.G = nx.DiGraph()

        self.initUI()

    def initFonts(self):
        """Ініціалізація шрифтів, кольорів"""
        self.color = "#8bb2d3"
        self.font_H1 = Font(self, name="font_H1", family="Verdana", size=18)
        self.font_p = Font(self, name="font_p", family="Verdana", size=14)
        self.font_work = Font(self, name="font_work", family="Verdana", size=10)

    def initUI(self):
        self.title("Графи")
        self.center()
        self["bg"] = self.color

        # Графічний інтерфейс

        self.frame_top = Frame(self, bg=self.color)
        self.lbl_v1 = Label(self.frame_top, text="Вершина 1",
                            bg=self.color, font="font_work")
        self.lbl_v2 = Label(self.frame_top, text="Вершина 2",
                            bg=self.color, font="font_work")
        self.entry_v1 = Entry(self.frame_top, font="font_work")
        self.lbl_arrow = Label(self.frame_top, text=" => ",
                               bg=self.color, font="font_work")
        self.entry_v2 = Entry(self.frame_top, font="font_work")
        self.btn_put = Button(self.frame_top, text="Додати ребро",
                              font="font_work", command=self.put)

        self.frame_graph = Frame(self, bg=self.color)
        self.lbl_graph = Label(self.frame_graph, text="Граф:",
                               font="font_p", bg=self.color)
        self.lbox_graph = Listbox(self.frame_graph, font="font_work", selectmode=EXTENDED)
        self.btn_read = Button(self.frame_graph, text="Зчитати з файлу",
                               font="font_work", command=self.read_)
        self.btn_del = Button(self.frame_graph, text="Видалити",
                              font="font_work", command=self.delete)

        self.frame_buttons = Frame(self, bg=self.color, bd=10)
        self.btn_ints = Button(self.frame_buttons, text="Сформувати матрицю інцидентності",
                                 font="font_work", command=self.ints)
        self.btn_sum = Button(self.frame_buttons, text="Граф, заданий матрицею суміжності",
                              font="font_work", command=self.sum)

        # grid

        self.frame_top.grid(row=0, column=0)
        self.lbl_v1.grid(row=0, column=0)
        self.lbl_v2.grid(row=0, column=2)
        self.entry_v1.grid(row=1, column=0)
        self.lbl_arrow.grid(row=1, column=1)
        self.entry_v2.grid(row=1, column=2)
        self.btn_put.grid(row=1, column=3)

        self.frame_graph.grid(row=1, column=0)
        self.lbl_graph.grid(row=0, column=0, columnspan=2)
        self.lbox_graph.grid(row=1, column=0, columnspan=2)
        self.btn_read.grid(row=2, column=0)
        self.btn_del.grid(row=2, column=1)

        self.frame_buttons.grid(row=2, column=0)
        self.btn_ints.grid(row=0, column=0)
        self.btn_sum.grid(row=0, column=1)

    def center(self):
        """Метод центрування вікна"""
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.wm_geometry("+%d+%d" % (x, y))

    def put(self):
        self.lbox_graph.delete(0, END)
        v1 = self.entry_v1.get()
        v2 = self.entry_v2.get()
        self.G.add_nodes_from((v1,v2))
        self.G.add_edge(v1,v2)
        for i in sorted(self.G.edges()):
            self.lbox_graph.insert(END, i)
        Matrix.G = self.G

    def read_(self):
        self.lbox_graph.delete(0, END)
        try:
            self.G = nx.read_edgelist(r"edges.txt", create_using=nx.DiGraph())
        except FileNotFoundError:
            self.lbox_graph.insert(END, "Файл відсутній")
        else:
            for i in sorted(self.G.edges()):
                self.lbox_graph.insert(END, i)
        Matrix.G = self.G

    def delete(self):
        for i in self.lbox_graph.curselection()[::-1]:
            self.G.remove_edge(self.lbox_graph.get(i)[0], self.lbox_graph.get(i)[-1])
            self.lbox_graph.delete(i)

    def ints(self):
        self.matrix_ints = Matrix(1)

    def sum(self):
        self.matrix_sum = Matrix(0)

class Matrix(Toplevel):

    def __init__(self, type):
        super().__init__()
        self.type = type
        if self.type == 1:
            self.type_of_matrix = "Матриця інцидентності"
        elif self.type == 0:
            self.type_of_matrix = "Матриця суміжності"
        self.color = "#8bb2d3"
        try:
            self.G = Matrix.G
        except AttributeError:
            messagebox.showerror("Помилка", "Граф не заданий ")
        else:
            self.initUI()
            self.matrix()

    def initUI(self):
        self.title(self.type_of_matrix)
        self["bg"] = self.color

        self.txt_matrix = Text(self, height=10)
        self.btn_graph = Button(self, text="Сформувати граф",
                                font="font_work", command=self.graph)

    #     grid

        self.txt_matrix.grid(row=0, column=0)
        self.btn_graph.grid(row=1, column=0)

        # self.protocol("WM_DELETE_WINDOW", self.messagequit)

    def matrix(self):
        """Відображення матриці"""

        self.txt_matrix.delete(0.0, END)

        # Створення матриці, заповненої нулями

        list_of_nodes = sorted(self.G.nodes())
        list_of_edges = sorted(self.G.edges())
        if self.type == 0:          # Суміжність
            length = len(list_of_nodes)
            list_ = [0] * length
            for i in range(length):
                list_[i] = [0] * length

        #     Заповнюємо "одиничками

            count_i = 0
            for i in list_of_nodes:
                count_j = 0
                for j in list_of_nodes:
                    if (i, j) in self.G.edges():
                        list_[count_i][count_j] = 1
                    count_j += 1
                count_i += 1

                # Додаємо імена в матрицю

            count = 0
            for i in list_of_nodes:
                list_[count].insert(0, i)
                count += 1
            list_.insert(0, list_of_nodes)
            list_[0].insert(0, " " * 4)

            # Виводимо в Text

            for i in list_:
                for j in i:
                    self.txt_matrix.insert(END, "{:^5}".format(j))
                self.txt_matrix.insert(END, "\n")

        elif self.type == 1:        # Інцидентність
            length1 = len(list_of_nodes)
            length2 = len(list_of_edges)
            list_ = [0] * length1
            for i in range(length1):
                list_[i] = [0] * length2

            count_i = 0
            for i in list_of_nodes:
                count_j = 0
                for j in list_of_edges:
                    if i == j[0]:
                        list_[count_i][count_j] = 1
                    elif i == j[1]:
                        list_[count_i][count_j] = -1
                    count_j += 1
                count_i += 1

            # Додаємо імена в матрицю

            count = 0
            for i in list_of_nodes:
                list_[count].insert(0, i)
                count += 1
            list_.insert(0, list_of_edges)
            list_[0].insert(0, " " * 4)

            # Виводимо в Text

            for i in list_:
                if list_.index(i) == 0:
                    for j in i:
                        self.txt_matrix.insert(END, "{0:^2}{1:^2}".format(j[0], j[-1])+" ")
                else:
                    for j in i:
                        self.txt_matrix.insert(END, "{:^5}".format(j))
                self.txt_matrix.insert(END, "\n")

    def graph(self):
        pos = nx.spring_layout(self.G)
        nx.draw_networkx_nodes(self.G, pos, nodelist=self.G.nodes())
        nx.draw_networkx_edges(self.G, pos, edgelist=self.G.edges())
        nx.draw_networkx_edges(self.G, pos, edgelist=self.G.selfloop_edges())
        nx.draw_networkx_labels(self.G, pos)


        plt.title("Граф")
        plt.show()

    def messagequit(self):
        """Метод визову messagebox для виходу з програми"""
        if messagebox.askyesno("Quit", "Завершити роботу?"):
            sys.exit()


if __name__ == "__main__":
    root = Window2()
    root.mainloop()
