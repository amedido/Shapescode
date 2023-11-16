# Create a stunning fractal graphic

import turtle
import colorsys
screen = turtle.Screen()
t = turtle.Turtle()

screen.title('Colored Fractal graphic')
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
screen.tracer(3,3)
screen.bgcolor('black')
t.speed(0)
t.hideturtle()

def draw_cross(x, y, length):
    t.up()
    t.goto(x-length/2, y-length/6)
    t.down()
    t.seth(0)
    h = (x**2 + y**2)**0.5/L * 1.7
    c = colorsys.hsv_to_rgb(h,1,1)
    t.fillcolor(c)
    t.begin_fill()
    for _ in range(4):
        t.forward(length/3)
        t.right(90)
        t.forward(length/3)
        t.left(90)
        t.forward(length/3)
        t.left(90)
    t.end_fill()

def draw(x, y, legnth, n):
    if n ==0:
        draw_cross(x, y, legnth)
        return
    draw(x, y, legnth/3, n-1)
    draw(x+legnth/3, y, legnth/3, n-1)
    draw(x-legnth/3, y, legnth/3, n-1)
    draw(x, y+legnth/3, legnth/3, n-1)
    draw(x, y-legnth/3, legnth/3, n-1)
L=1600
draw()