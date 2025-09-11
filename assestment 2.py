import turtle
from turtle import *
t = Turtle()
t.speed(50)
for i in range(60):
    def star (x,y):
        for i in range(5):
            t.forward(x)
            t.right(y)
        t.right(5)
       
star (5,144)

def addstar(irange):
    length = 5
    for i in range(irange):
        star(length, 144)
        length += 5
addstar(60)

turtle.done()