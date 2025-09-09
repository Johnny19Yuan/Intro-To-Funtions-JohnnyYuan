import turtle
from turtle import *
t = Turtle()


def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200)

def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
equal(200)

def angle(x):
    t.forward(125)
    t.left(x)
    t.forward(100)
    t.left(x)
    t.forward(125)
    t.left(x)
    t.forward(100)
    t.left(x)
angle(90)


turtle.done()
