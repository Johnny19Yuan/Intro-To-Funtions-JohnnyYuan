import turtle
from turtle import *
t = Turtle()

def square (x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square (100,90)
# makes squares size double
def doublesquare(irange):
    length = 25
    for i in range(irange):
        square(length, 90)
        length = length * 2
doublesquare(5)

turtle.done()