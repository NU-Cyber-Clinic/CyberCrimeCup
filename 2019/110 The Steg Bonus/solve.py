from PIL import Image

im = Image.open('see-you-soon.png')

string = ""

width, height = im.size
for y in range(height):
	for x in range(width):
		r,g,b = im.getpixel((x,y))
		if (r == 255):
			string += "1"
		if (r == 0):
			string += "0"

print(string)