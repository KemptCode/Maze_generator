from PIL import Image, ImageDraw    # To edit Pictures
from prims import prims_grid_dimensions_to_random_edges
import time
before_time = time.time()

# Create minimum-spanning tree for maze
X_WIDTH = 64
Y_HEIGHT = 64

edges = prims_grid_dimensions_to_random_edges(X_WIDTH, Y_HEIGHT)
after_time = time.time()
print(f"time for Prim's algorithm: {after_time - before_time}")

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
img.save('maze_14.png')
