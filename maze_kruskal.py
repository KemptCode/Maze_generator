import pygame
import random

# NOTE: This doesn't go connect two nodes it has already visited and doesn't complete
# the definition of Kruscal's algorithm

nodes = {}
potentialEdges = [] # Sorted list by weights
edges = []
visited = set()

# Add nodes to the 
for i in range(4):
    for j in range(4):
        myNum = random.randint(0,100)
        nodes[(i, j)] = myNum
        # Looking one up and then looking back left
        if w2 := nodes.get((i-1,j), None):
            potentialEdges.append([(myNum + w2), (i-1, j), (i,j)])
        if w3 := nodes.get((i,j-1), None):
            potentialEdges.append([(myNum + w3), (i, j-1), (i,j)])

potentialEdges.sort() # Sort randomly weighted edges

for pEdge in potentialEdges:
    if pEdge[1] not in visited or pEdge[2] not in visited:
        edges.append(pEdge)
        visited.add(pEdge[1])
        visited.add(pEdge[2])

# pygame represenation
pygame.init()

S_WIDTH = 800
S_HEIGHT = 600
running = True
scale = 50

screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # exit()

    # Represent the nodes
    for node in nodes:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(tuple(map(lambda x: x * scale, node)),(6, 6)))

    # Represent the edges
    for edge in edges:
        pygame.draw.line(screen, (150,80,100), tuple(map(lambda x: x * scale, edge[1])), tuple(map(lambda x: x * scale, edge[2])), 5)

    # thisValue = pygame.Rect((10,10),(20,20))
    # pygame.draw.rect(screen,(100,100,100),thisValue)
    pygame.display.update()
