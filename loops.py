import turtle
from turtle import *
t = Turtle()
t.speed(10)

for i in range(4):
    def square(x):
        t.forward(x)
        t.left(90)
    square(100)

for i in range(3):
    def triangle(y):
        t.forward(y)
        t.left(120)
    triangle(100)


for i in range(60):
    for i in range(4):
        def square2(z):
            t.forward(z)
            t.left(90)
        square2(100)
    t.left(5)
turtle.done()