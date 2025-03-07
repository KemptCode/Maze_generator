import random                       # For a different maze each time
import heapq

def prims_grid_dimensions_to_random_edges(x_width, y_height):
    TOTAL_NODES = x_width * y_height
    nodes = {}              # Total nodes
    potentialEdges = []     # from where we are
    edges = []              # Final product of where we choose for the maze to go
    visited = set()         # Don't make a loop

    # Adds nodes -- Creates a grid
    for i in range(x_width):
        for j in range(y_height):
            myNum = random.randint(0,100)
            nodes[(i, j)] = myNum


    # Starting from 0, 0 # To be random in a future version
    visited.add((0,0))
    potentialEdges.append((nodes[(0,0)] + nodes[(0,1)],(0,0),(0,1)))
    potentialEdges.append((nodes[(0,0)] + nodes[(1,0)],(0,0),(1,0)))
    heapq.heapify(potentialEdges)

    # Keep looping until we have a minimum spanning tree, visiting all nodes
    while len(visited) != TOTAL_NODES:
        currentEdge = heapq.heappop(potentialEdges)
        if currentEdge[1] not in visited or currentEdge[2] not in visited: 
            # ADD it to the edges we have chosen
            edges.append(currentEdge)
            
            # if it was the first one
            newNode = currentEdge[1] if currentEdge[1] not in visited else currentEdge[2]

            # add the second one
            visited.add(newNode)

            # check around to: add edges to potential edges
            #up
            oneAbove = (newNode[0], newNode[1] - 1)
            if oneAbove in nodes and oneAbove not in visited:
                heapq.heappush(potentialEdges, (nodes.get(newNode) + nodes.get(oneAbove), newNode, oneAbove))
            #right
            oneRight = (newNode[0] + 1, newNode[1])
            if oneRight in nodes and oneRight not in visited:
                heapq.heappush(potentialEdges, (nodes.get(newNode) + nodes.get(oneRight), newNode, oneRight))
            #left
            oneLeft = (newNode[0] - 1, newNode[1])
            if oneLeft in nodes and oneLeft not in visited:
                heapq.heappush(potentialEdges, (nodes.get(newNode) + nodes.get(oneLeft), newNode, oneLeft))
            #down
            oneDown = (newNode[0], newNode[1] + 1)
            if oneDown in nodes and oneDown not in visited:
                heapq.heappush(potentialEdges, (nodes.get(newNode) + nodes.get(oneDown), newNode, oneDown))

    return edges