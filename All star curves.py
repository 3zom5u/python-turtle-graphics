from turtle import *
import time
import random
from random import randint
print("how many points do you want your star to have?(it can be anything!!!)")
points = int(input())
print("how big do you want it?(100-350 but gets slower the bigger the size")
distance = int(input())
turn = 360/points
listnumber = 0
listnumber2 = distance
line1x = []
line1y = []
line2x = []
line2y = []
penup()
speed(0)
left(90)
#hideturtle()
for i in range(points):#to make each part of the star
    for i in range(distance + 1):#doing line1 positions
        forward(1)
        line1x.append(xcor())
        line1y.append(ycor())
    goto(0,0)
    right(turn)
    for i in range(distance + 1):#doing line2 positions
        forward(1)
        line2x.append(xcor())
        line2y.append(ycor())
    goto(0,0)
    pendown()
    for i in range(distance + 1):#drawing
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
    listnumber2 = distance









    