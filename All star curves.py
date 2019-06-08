from turtle import *
import time
import random
from random import randint
import mlib
from mlib import points
def thething():
    points = int(input("how many points would you like your star to have?(it can be anything!)"))
    distance = int(input("how big would you like your star to be?(200-350 recommended)"))
    turn = 360/points
    inc = distance/100
    listnumber = 0
    listnumber2 = 99
    line1x = []
    line1y = []
    line2x = []
    line2y = []
    speed(0)
    left(90)
    hideturtle()
    for i in range(points):#to make each part of the star
        penup()
        for i in range(100):#doing line1 positions
            forward(inc)
            line1x.append(xcor())
            line1y.append(ycor())
        goto(0,0)
        right(turn)
        for i in range(100):#doing line2 positions
            forward(inc)
            line2x.append(xcor())
            line2y.append(ycor())
        goto(0,0)
        pendown()
        for i in range(100):#drawing
            goto(line1x[listnumber],line1y[listnumber])
            goto(line2x[listnumber2],line2y[listnumber2])
            listnumber = listnumber + 1
            listnumber2 = listnumber2 - 1
            goto(0,0)
        line1x.clear()
        line1y.clear()
        line2x.clear()
        line2y.clear()
        listnumber = 0
        listnumber2 = 99
thething()




    
