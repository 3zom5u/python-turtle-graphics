#set zone for turtle (341.50,288.00)
from turtle import *
import time
import random
from random import randint
r = lambda: random.randint(0,255)
hexcolour = '#%02X%02X%02X' % (r(),r(),r())
speed(0)
width(50)
poscheckerx = 0
poscheckery = 0
sety(0)
setx(0)
while True:
    pencolor(hexcolour)
    right(randint(0, 180))
    forward(20)
    poscheckerx = round(xcor(), 5)
    poscheckery = round(ycor(), 5)
    if poscheckerx >= 311.50 or poscheckerx <= -321.50:
        right(180)
        forward(30)
    if poscheckery >= 278.00 or poscheckery <= -268.00:
        right(180)
        forward(30)
    hexcolour = '#%02X%02X%02X' % (r(),r(),r())
