from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from collections import OrderedDict
import networkx as nx
import matplotlib.pyplot as plt

class Painter(Tk):

    def __init__(self):

        super().__init__()
        self.initFonts()
        self.initUI()

        self.colors = ["red", "blue", "green", "yellow", "orange", "purple", "grey", "darkgrey"]
        self.G = nx.Graph()

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

        self.btn_draw = Button(self, text="Розфарбувати",
                                  font="font_work", command=self.paint)

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

        self.btn_draw.grid(row=2, column=0)

    def messagequit(self):
        """Метод визову messagebox для виходу з програми"""
        if messagebox.askyesno("Quit", "Завершити роботу?"):
            sys.exit()

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

    def read_(self):
        self.lbox_graph.delete(0, END)
        try:
            self.G = nx.read_edgelist(r"edges.txt", create_using=nx.Graph())
        except FileNotFoundError:
            self.lbox_graph.insert(END, "Файл відсутній")
        else:
            for i in sorted(self.G.edges()):
                self.lbox_graph.insert(END, i)

    def delete(self):
        for i in self.lbox_graph.curselection()[::-1]:
            self.G.remove_edge(self.lbox_graph.get(i)[0], self.lbox_graph.get(i)[-1])
            self.lbox_graph.delete(i)

    def paint(self):
        colorsDictionary = dict()
        degDictionary = self.G.degree()


        sortArr = []
        for i in OrderedDict(sorted(degDictionary.items(), key=lambda x: x[-1], reverse=True)):
            sortArr.append(i)

        for i in range(0, len(sortArr)):
            # i - current color
            if sortArr[i] in colorsDictionary:
                continue
            colorsDictionary.update([(sortArr[i], i)])
            stack = []
            for j in sortArr:
                flag = False
                if stack:
                    for k in stack:
                        if ((k, j) in self.G.edges() or (j, k) in self.G.edges()):
                            flag = True
                if (j in colorsDictionary
                    or (sortArr[i], j) in self.G.edges()
                    or (j, sortArr[i]) in self.G.edges()
                    or flag):
                    continue

                colorsDictionary.update([(j, i)])
                stack.append(j)

            if len(colorsDictionary.keys()) == len(sortArr):
                break
        self.graph(colorsDictionary)

    def graph(self, colorsDictionary):
        colorsDictionary = colorsDictionary
        pos = nx.spring_layout(self.G)
        for i in colorsDictionary.keys():
            nx.draw_networkx_nodes(self.G, pos, nodelist=[i], node_color=self.colors[colorsDictionary[i]])
        nx.draw_networkx_edges(self.G, pos, edgelist=self.G.edges())
        nx.draw_networkx_labels(self.G, pos)

        plt.title("Розфарбований граф (евристичний алгоритм)")
        plt.show()

if __name__ == "__main__":
    root = Painter()
    root.mainloop()
