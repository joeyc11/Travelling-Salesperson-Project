#import main
import math
import nodeStructure as NS

def greedy(plt):
    #greedyAlgorithm
    availableNodes = NS.nodes.copy()
    currentNode = availableNodes[0]
    for i in range(NS.numNodes-1):
        shortest = 400
        for j in availableNodes:
            current = math.sqrt((currentNode.x-j.x)**2+(currentNode.y-j.y)**2)
            if current < shortest:
                shortest = current
                nextNode = j
        NS.connectNodes(currentNode, nextNode, plt)   

        #leave one node left so we can connect it to the home node
        if i < NS.numNodes-2: availableNodes.remove(nextNode)
        currentNode = nextNode
        
    #connect the final node back to the home node
    NS.connectNodes(availableNodes[0], NS.nodes[0], plt)