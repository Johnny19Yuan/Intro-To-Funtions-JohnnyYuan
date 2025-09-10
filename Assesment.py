import turtle
from turtle import *
T = Turtle()

def squaresize(startlength):
    for i in range(60):
        for i in range(4):
            T.forward(x)
            T.left(90)
    squaresize(5)



def addsquare(irange):
    startlength = 5
    for i in range(irange):
        squaresize(startlength, 90)
        startlength += 5
addsquare(5)