import main
import math

def greedyAlgorithm():
    #greedyAlgorithm
    availableNodes = main.nodes.copy()
    currentNode = availableNodes[0]
    for i in range(main.numNodes-1):
        shortest = 400
        for j in availableNodes:
            current = math.sqrt((currentNode.x-j.x)**2+(currentNode.y-j.y)**2)
            if current < shortest:
                shortest = current
                nextNode = j
        main.connectNodes(currentNode, nextNode)   

        #leave one node left so we can connect it to the home node
        if i < main.numNodes-2: availableNodes.remove(nextNode)
        currentNode = nextNode
        
    #connect the final node back to the home node
    main.connectNodes(availableNodes[0], main.nodes[0])