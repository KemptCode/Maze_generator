from PIL import Image, ImageDraw    # To edit Pictures
import random                       # For a different maze each time

X_WIDTH = 64    # This changes everything in the code
Y_HEIGHT = 64

# NOTE: Attempt 1.0 for Prim's algorithm to make a viable maze

nodes = {}              # Total nodes
nodesInReach = set()    # Adjacent nodes to where we have connected to and have not connected yet
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
            potentialEdges.append((nodes.get(newNode) + nodes.get(oneAbove), newNode, oneAbove))
        #right
        oneRight = (newNode[0] + 1, newNode[1])
        if oneRight in nodes and oneRight not in visited:
            nodesInReach.add(oneRight)
            potentialEdges.append((nodes.get(newNode) + nodes.get(oneRight), newNode, oneRight))
        #left
        oneLeft = (newNode[0] - 1, newNode[1])
        if oneLeft in nodes and oneLeft not in visited:
            nodesInReach.add(oneLeft)
            potentialEdges.append((nodes.get(newNode) + nodes.get(oneLeft), newNode, oneLeft))
        #down
        oneDown = (newNode[0], newNode[1] + 1)
        if oneDown in nodes and oneDown not in visited:
            nodesInReach.add(oneDown)
            potentialEdges.append((nodes.get(newNode) + nodes.get(oneDown), newNode, oneDown))



# pillow represenation
SCALE = 2
S_WIDTH = X_WIDTH * SCALE - 1
S_HEIGHT = Y_HEIGHT * SCALE - 1

img = Image.new('RGB',(S_WIDTH,S_HEIGHT))
draw = ImageDraw.Draw(img)

# Represent the edges
for edge in edges:
    draw.line((tuple(map(lambda x: x * SCALE, edge[1])), tuple(map(lambda x: x * SCALE, edge[2]))),fill='White', width=1)

# Save the picture
img.save('maze_10.png')