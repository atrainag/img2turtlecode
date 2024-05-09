from PIL import Image
import numpy as np

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b).upper()

filename = "ditto"
format = "png"
im = Image.open(f"{filename}.{format}")
data = im.getdata()
pixels = list(data) 
pixels = np.array(pixels,dtype='uint8')

w = im.size[0]
h = im.size[1]

pixels = pixels.reshape(h,w,3)
f = open(f"{filename}.py","w")

pix = 2 

init = f'''import turtle 
p = turtle.Pen()
p.speed('fastest')
p.up()
p.setpos(-500,325)
p.down()
def draw_pixel(color,length):
    p.color(color)
    p.begin_fill()
    for i in range(1,5):
        p.fd({pix}*(i%2)*(length-1)+{pix})
        p.rt(90)
    p.end_fill()
'''
f.write(init)
for i in range(h):
    cur = np.array([-1,-1,-1])
    num = 1
    output = 0
    for j in range(w):
        if(np.array_equal(cur,[-1,-1,-1])):
            cur = pixels[i,j]
            if(j == w-1 or not np.array_equal(cur,pixels[i,j+1])):
               output = 1 
            else:   
                num += 1
        elif(j!=w-1 and np.array_equal(cur,pixels[i,j+1])):
            num += 1
        else:
            output = 1
        if(output):
            pixel = pixels[i,j]
            hxcol = rgb2hex(*pixel)
            f.write(f"draw_pixel(\"{hxcol}\",{num})\np.fd({pix*num})\n") 
            num = 1
            cur = np.array([-1,-1,-1])
            output = 0
    pos = w*pix
    f.write("\np.up()\n")
    f.write(f"p.rt(180)\np.fd({pos})\np.lt(90)\np.fd({pix})\np.lt(90)\n")
    f.write("p.down()\n")

f.write("#turtle.update()\nturtle.done()")
