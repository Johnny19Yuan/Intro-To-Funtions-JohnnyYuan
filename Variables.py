import turtle
from turtle import *
t = Turtle()

def square (x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square (100,90)

turtle.done()