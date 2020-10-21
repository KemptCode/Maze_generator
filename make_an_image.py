from PIL import Image, ImageDraw

img = Image.new('RGB',(50,50))

draw = ImageDraw.Draw(img)
draw.rectangle(((20,0),(20,10)),fill='Red')

img.save('maze.png')

