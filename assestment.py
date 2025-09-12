import turtle
from turtle import *
t = Turtle()
t.speed(100)
for i in range(60):
    def square (x,y):
        for i in range(4):
            t.forward(x)
            t.left(y)
        t.right(5)
       
square (5,90)

def addsquare(irange):
    length = 5
    for i in range(irange):
        square(length, 90)
        length += 5
addsquare(60)

turtle.done()