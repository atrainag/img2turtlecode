import turtle 
p = turtle.Pen()
p.speed('fastest')
p.up()
p.setpos(-375,320)
p.down()
def draw_pixel(color,length):
    p.color(color)
    p.begin_fill()
    for i in range(1,5):
        p.fd(2*(i%2)*(length-1)+2)
        p.rt(90)
    p.end_fill()
for i in range(100):
    draw_pixel("green",10)
    p.fd(10)
    draw_pixel("green",10)
    p.fd(10)
    draw_pixel("green",10)
    p.fd(10)
    draw_pixel("green",10)
    p.fd(10)
    draw_pixel("green",10)
    p.fd(10)
    draw_pixel("green",10)
    p.fd(10)
turtle.done()
