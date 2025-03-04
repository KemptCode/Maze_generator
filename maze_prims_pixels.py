from PIL import Image, ImageDraw    # To edit Pictures
import random                       # For a different maze each time
import time
before_time = time.time()

X_WIDTH = 64    # This changes everything in the code
Y_HEIGHT = 64
TOTAL_NODES = X_WIDTH * Y_HEIGHT

# NOTE: Attempt 1.0 for Prim's algorithm to make a viable maze

nodes = {}              # Total nodes
potentialEdges = []     # from where we are
edges = []              # Final product of where we choose for the maze to go
visited = set()         # Don't make a loop

# Adds nodes -- Creates a grid
for i in range(X_WIDTH):
    for j in range(Y_HEIGHT):
        myNum = random.randint(0,100)
        nodes[(i, j)] = myNum


# Starting from 0, 0 # To be random in a future version
visited.add((0,0))
potentialEdges.append((nodes[(0,0)] + nodes[(0,1)],(0,0),(0,1)))
potentialEdges.append((nodes[(0,0)] + nodes[(1,0)],(0,0),(1,0)))

# Keep looping till we have nothing else to add
while len(visited) != TOTAL_NODES:
    potentialEdges.sort()

    currentEdge = potentialEdges.pop(0)
    if currentEdge[1] not in visited or currentEdge[2] not in visited: 
        # ADD it to the edges we have chosen
        edges.append(currentEdge)
        
        # if it was the first one
        newNode = currentEdge[1] if currentEdge[1] not in visited else currentEdge[2]

        # add the second one
        visited.add(newNode)

        # check around to:
        # add edges to potential edges
        #up
        oneAbove = (newNode[0], newNode[1] - 1)
        if oneAbove in nodes and oneAbove not in visited:
            potentialEdges.append((nodes.get(newNode) + nodes.get(oneAbove), newNode, oneAbove))
        #right
        oneRight = (newNode[0] + 1, newNode[1])
        if oneRight in nodes and oneRight not in visited:
            potentialEdges.append((nodes.get(newNode) + nodes.get(oneRight), newNode, oneRight))
        #left
        oneLeft = (newNode[0] - 1, newNode[1])
        if oneLeft in nodes and oneLeft not in visited:
            potentialEdges.append((nodes.get(newNode) + nodes.get(oneLeft), newNode, oneLeft))
        #down
        oneDown = (newNode[0], newNode[1] + 1)
        if oneDown in nodes and oneDown not in visited:
            potentialEdges.append((nodes.get(newNode) + nodes.get(oneDown), newNode, oneDown))
after_time = time.time()
print(f"time diff: {after_time - before_time}")


# Image represenation
SCALE = 2
S_WIDTH = X_WIDTH * SCALE - 1
S_HEIGHT = Y_HEIGHT * SCALE - 1

img = Image.new('RGB',(S_WIDTH,S_HEIGHT))
draw = ImageDraw.Draw(img)

# Represent the edges
for edge in edges:
    draw.line((tuple(map(lambda x: x * SCALE, edge[1])), tuple(map(lambda x: x * SCALE, edge[2]))),fill='White', width=1)

# Save the picture
img.save('maze_11.png')
