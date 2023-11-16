import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()

n=50
h=0
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.forward(1*2)
    t.left(145)