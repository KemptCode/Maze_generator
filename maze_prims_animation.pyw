import pygame
import random
import time

# NOTE: Attempt 1.0 for Prim's algorithm to make a viable maze

nodes = {}
nodesInReach = set()
visited = set()
potentialEdges = [] # from where we are
edges = []              


# pygame represenation -- VARIABLES
pygame.init()

S_WIDTH = 800
S_HEIGHT = 600
running = True
scale = 20

screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))



# Add nodes to the 
for i in range(40):
    for j in range(30):
        myNum = random.randint(0,100)
        nodes[(i, j)] = myNum


# Starting from 0, 0 # To be random in a future version
visited.add((0,0))
nodesInReach.add((0,1))
nodesInReach.add((1,0))
potentialEdges.append((nodes[(0,0)] + nodes[(0,1)],(0,0),(0,1)))
potentialEdges.append((nodes[(0,0)] + nodes[(1,0)],(0,0),(1,0)))

# Keep looping till we have nothing else to add
while len(nodesInReach) > 0:
    potentialEdges.sort()

    currentEdge = potentialEdges.pop(0)
    if currentEdge[1] in nodesInReach or currentEdge[2] in nodesInReach: 
        # ADD it to the edges we have chosen
        edges.append(currentEdge)
        
        # if it was the first one
        # CONDITIONAL MOVE
        newNode = currentEdge[1] if currentEdge[1] not in visited else currentEdge[2]

        # add the second one
        visited.add(newNode)
        # remove from reachable nodes
        nodesInReach.remove(newNode) # may raise an error (switch to discard???)

        # check around to:
        # add reachable nodes AND # add edges to potential edges
        #up
        oneAbove = (newNode[0], newNode[1] - 1)
        if oneAbove in nodes and oneAbove not in visited:
            nodesInReach.add(oneAbove)
            potentialEdges.append(tuple([nodes.get(newNode) + nodes.get(oneAbove), newNode, oneAbove]))
        #right
        oneRight = (newNode[0] + 1, newNode[1])
        if oneRight in nodes and oneRight not in visited:
            nodesInReach.add(oneRight)
            potentialEdges.append(tuple([nodes.get(newNode) + nodes.get(oneRight), newNode, oneRight]))
        #left
        oneLeft = (newNode[0] - 1, newNode[1])
        if oneLeft in nodes and oneLeft not in visited:
            nodesInReach.add(oneLeft)
            potentialEdges.append(tuple([nodes.get(newNode) + nodes.get(oneLeft), newNode, oneLeft]))
        #down
        oneDown = (newNode[0], newNode[1] + 1)
        if oneDown in nodes and oneDown not in visited:
            nodesInReach.add(oneDown)
            potentialEdges.append(tuple([nodes.get(newNode) + nodes.get(oneDown), newNode, oneDown]))

    # PYGAME ----- RENDERING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # exit()

    # Represent the nodes
    for node in nodes:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(tuple(map(lambda x: x * scale, node)),(6, 6)))

    # Represent the edges
    for edge in edges:
        pygame.draw.line(screen, (200,200,200), tuple(map(lambda x: x * scale, edge[1])), tuple(map(lambda x: x * scale, edge[2])), 5)

    pygame.draw.line(screen, (255,0,0), tuple(map(lambda x: x * scale, edges[-1][1])), tuple(map(lambda x: x * scale, edges[-1][2])), 5)
    
    time.sleep(0.006)
    pygame.display.update()
