import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2TkAgg
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure

import random

import greedyAlgorithm
import nodeStructure as NS

import tkinter as tk
from tkinter import ttk


greedyGraph = Figure(figsize=(5,5), dpi=100)
a = greedyGraph.add_subplot(111)

class TravellingSalespersonApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self, default=folderLocation+"FantasyScraperIcon.ico")
        tk.Tk.wm_title(self, "Travelling Salesperson")
        
        #frame1 = SelectPage(container, self)
        

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        
        container.grid_rowconfigure(0, weight=100)
        #container.grid_rowconfigure(1, weight=100)
        container.grid_columnconfigure(0, weight=100)

        

        self.frames = {}

        

        for F in (SelectPage, GreedyPage):
            
            frame = F(container, self)
            self.frames[F] = frame
            frame.pack(expand=TRUE)
            #frame.grid(row=1, column=0, sticky="nsew")

        self.show_frame(SelectPage)
        #self.show_frame(SelectPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class SelectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        button1 = ttk.Button(self, text="Agree",
                            command=lambda: [controller.show_frame(GreedyPage), controller.show_frame(SelectPage)])
        button1.pack(side=LEFT, anchor=NE)

        button2 = ttk.Button(self, text="Agree2",
                            command=lambda: controller.show_frame(GreedyPage))
        button2.pack(side=LEFT, anchor=NE)


class GreedyPage(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager

        canvas = FigureCanvasTkAgg(greedyGraph, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


#animation function used to colour points
def animate(i):
    #plt.style.use('seaborn')
    greedyAlgorithm.greedy(plt)
    plt.scatter(NS.xVals, NS.yVals, c=NS.colours, cmap='summer',
                edgecolor='black', alpha=0.75)

    plt.title('Greedy Algorithm')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.tight_layout()


        


#create all  the nodes
i = 1
while i < NS.numNodes - 1:
    x = random.randrange(*NS.rangeX)
    y = random.randrange(*NS.rangeY)
    newNode = NS.node(x, y, False, i)
    NS.nodes.append(newNode)
    NS.xVals.append(x)
    NS.yVals.append(y)
    NS.colours.append(newNode.colour)
    i += 1

#call animation to change colours of nodes
ani = FuncAnimation(greedyGraph, animate, interval = 300)

greedyAlgorithm.greedy(plt)
TravellingSalespersonApp.mainloop()
#plt.show()