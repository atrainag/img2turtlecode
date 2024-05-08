from PIL import Image
import numpy as np

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b).upper()
filename = "umbreon"
im = Image.open(f"{filename}.jpeg")

pixels = list(im.getdata())
pixels = np.array(pixels,dtype='uint8')

w = im.size[0]
h = im.size[1]

pixels = pixels.reshape(h,w,3)
f = open(f"{filename}.py","w")

init = '''import turtle 
p = turtle.Pen()
#turtle.tracer(0,0)
p.speed('fastest')
p.up()
p.setpos(-375,320)
p.down()
def draw_pixel(color):
    p.color(color)
    p.begin_fill()
    for i in range(4):
        p.fd(2)
        p.rt(90)
    p.end_fill()
'''

f.write(init)
pix = 2 
for i in range(h):
    for j in range(w):
        pixel = pixels[i,j]
        hxcol = rgb2hex(*pixel)
        f.write(f"draw_pixel(\"{hxcol}\")\np.fd({pix})\n") 
    pos = w*pix
    f.write(f"\np.rt(180)\np.fd({pos})\np.lt(90)\np.fd({pix})\np.lt(90)\n")

f.write("#turtle.update()\nturtle.done()")
