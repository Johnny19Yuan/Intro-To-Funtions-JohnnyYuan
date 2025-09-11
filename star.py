import turtle
from turtle import *
t = Turtle()

for i in range(5):
    def star(x):
        t.forward(x)
        t.right(144)
    star(100)

turtle.done()