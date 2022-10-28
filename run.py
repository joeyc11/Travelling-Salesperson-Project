
from bauhaus import Encoding, proposition, constraint, utils
#from bauhaus.utils import count_solutions, likelihood

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



# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class BasicPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"


# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
@constraint.at_least_one(E)
@proposition(E)
class FancyPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

# Call your variables whatever you want
a = BasicPropositions("a")
b = BasicPropositions("b")   
c = BasicPropositions("c")
d = BasicPropositions("d")
e = BasicPropositions("e")
# At least one of these will be true
x = FancyPropositions("x")
y = FancyPropositions("y")
z = FancyPropositions("z")


# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    # Add custom constraints by creating formulas with the variables you created. 
    E.add_constraint((a | b) & ~x)
    # Implication
    E.add_constraint(y >> z)
    # Negate a formula
    E.add_constraint(~(x & y))
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BasicPropositions, but you want to enforce it for a, b, and c.:
    constraint.add_exactly_one(E, a, b, c)

    return E


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    #print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    #for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
    #    print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()