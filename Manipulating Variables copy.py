import turtle
from turtle import *
t = Turtle()

def square (x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square (100,90)
# makes squares size +25
def addsquare(irange):
    length = 25
    for i in range(irange):
        square(length, 90)
        length += 25
addsquare(5)

turtle.done()