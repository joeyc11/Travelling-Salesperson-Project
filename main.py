import pandas as pd
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation

import random

rangeX = (0, 200)
rangeY = (0, 200)
numNodes = 20  
totalDistance = 0

#animation function used to colour points
def animate(i):
    #plt.style.use('seaborn')
    plt.scatter(xVals, yVals, c=colours, cmap='summer',
                edgecolor='black', alpha=0.75)

    plt.title('Greedy Algorithm')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.tight_layout()


#adding lines to plot
def connectNodes(node1, node2):
    plt.plot([node1.x,node2.x],[node1.y,node2.y],color = "black")
    colours[node2.nodeNum] = "green"
    plt.waitforbuttonpress()
    


class node:
    def __init__(self, x, y, home, nodeNum):
        self.nodeNum = nodeNum
        self.x = x
        self.y = y
        self.home = home
        self.colour = "red"
        if self.home == True:
            self.colour = "yellow"
        self.visited = False
        

#create homoe node and initialize lists
newNode = node(0, 0, True, 0) 
nodes = [newNode]
xVals =  [newNode.x]
yVals = [newNode.y]
colours = [newNode.colour]

#create all  the nodes
i = 1
while i < numNodes - 1:
    x = random.randrange(*rangeX)
    y = random.randrange(*rangeY)
    newNode = node(x, y, False, i)
    nodes.append(newNode)
    xVals.append(x)
    yVals.append(y)
    colours.append(newNode.colour)
    i += 1

#call animation to change colours of nodes
ani = FuncAnimation(plt.gcf(), animate, interval = 300)

availableNodes = nodes.copy()
currentNode = availableNodes[0]
for i in range(numNodes-1):
    shortest = 400
    for j in availableNodes:
        current = math.sqrt((currentNode.x-j.x)**2+(currentNode.y-j.y)**2)
        if current < shortest:
            shortest = current
            nextNode = j
    connectNodes(currentNode, nextNode)   

    #leave one node left so we can connect it to the home node
    if i < numNodes-2: availableNodes.remove(nextNode)
    currentNode = nextNode
    
#connect the final node back to the home node
connectNodes(availableNodes[0], nodes[0])

#plt.show()