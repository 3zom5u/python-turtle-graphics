from turtle import *
speed(0)
from random import randint
shape1 = (randint(0, 90))
shape2 = (randint(0, 90))
shape3 = (randint(0, 90))
shape4 = (randint(0, 90))
def patten():
    for counter in range(100):
        for counter in range(100):
            pencolor("red")
            forward(50)
            right(shape1)
        for counter in range(100):
            pencolor("blue")
            forward(50)
            right(shape2)
        for counter in range(100):
            pencolor("orange")
            forward(50)
            right(shape3)
        for counter in range(100):
            pencolor("green")
            forward(50)
            right(shape4)
patten()