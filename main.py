import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
import greedyAlgorithm
import random

import greedyAlgorithm
import nodeStructure as NS



#animation function used to colour points
def animate(i):
    #plt.style.use('seaborn')
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
ani = FuncAnimation(plt.gcf(), animate, interval = 300)

greedyAlgorithm.greedy(plt)

#plt.show()