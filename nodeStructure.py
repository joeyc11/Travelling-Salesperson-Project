
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


rangeX = (0, 200)
rangeY = (0, 200)
numNodes = 20  
totalDistance = 0

#create homoe node and initialize lists
newNode = node(0, 0, True, 0) 
nodes = [newNode]
xVals =  [newNode.x]
yVals = [newNode.y]
colours = [newNode.colour]

#adding lines to plot
def connectNodes(node1, node2, plt):
    plt.plot([node1.x,node2.x],[node1.y,node2.y],color = "black")
    colours[node2.nodeNum] = "green"
    plt.waitforbuttonpress()


        