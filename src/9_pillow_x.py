from PIL import Image, ImageDraw

size = 100
img = Image.new("RGB", (size, size), "white")
draw = ImageDraw.Draw(img)

for i in range(size):
    draw.point((i, i), fill="black")
    draw.point((i, size - i - 1), fill="black")

img.show()

