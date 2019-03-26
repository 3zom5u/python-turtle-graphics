from turtle import *
import time
import random
speed(0)
hideturtle()
size = 0
inc = 0
r = lambda: random.randint(0,255)
def size_decider():
    global size
    global inc
    hexcolour = '#%02X%02X%02X' % (r(),r(),r())
    print("how big would you like it?(350-100 recomended)")
    size = int(input())
    inc = size / 100 * 1
    time.sleep(5)

def eight_point_star():
    global size
    global inc
    time.sleep(5)
    x = 0
    x2 = 0
    y = size
    y2 = 0
    while y >= 0:
        goto(x,x2)
        goto(0,y)
        y = y - inc
        x = x + inc
        x2 = x2 + inc
        y2 = y2 + inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    x = size
    x2 = 0
    y = 0
    y2 = 0
    while x >= 0:
        goto(x,0)
        goto(y2,y)
        y = y + inc
        x = x - inc
        x2 = x2 + inc
        y2 = y2 + inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    x = size
    x2 = 0
    y = 0
    y2 = 0
    while x >= 0:
        goto(x,0)
        goto(y2,y)
        y = y - inc
        x = x - inc
        x2 = x2 + inc
        y2 = y2 + inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    x = 0
    x2 = 0
    y = size - (size *2)
    y2 = 0
    while y <= 0:
        goto(x,x2)
        goto(0,y)
        y = y + inc
        x = x + inc
        x2 = x2 - inc
        y2 = y2 + inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    x = 0
    x2 = 0
    y = size - (size *2)
    y2 = 0
    while y <= 0:
        goto(x,x2)
        goto(0,y)
        y = y + inc
        x = x - inc
        x2 = x2 - inc
        y2 = y2 + inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    x = size - (size * 2)
    x2 = 0
    y = 0
    y2 = 0
    while x <= 0:
        goto(x,0)
        goto(y2,y)
        y = y - inc
        x = x + inc
        x2 = x2 - inc
        y2 = y2 - inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    x = size - (size * 2)
    x2 = 0
    y = 0
    y2 = 0
    while x <= 0:
        goto(x,0)
        goto(y2,y)
        y = y + inc
        x = x + inc
        x2 = x2 - inc
        y2 = y2 - inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    x = 0
    x2 = 0
    y = size
    y2 = 0
    while y >= 0:
        goto(x,x2)
        goto(0,y)
        y = y - inc
        x = x - inc
        x2 = x2 + inc
        y2 = y2 + inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    menu()

def cyrcle_square():
    global size
    global inc
    time.sleep(5)
    y = size
    x2 = size
    x = size - size
    y2 = size
    penup()
    goto(x,y2)
    pendown()
    while y >= 0:
        goto(x,y2)
        goto(x2,y)
        y = y - inc
        x = x + inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    y = 0
    x2 = size - (size * 2)
    x = size - (size * 2)
    y2 = size
    penup()
    goto(x,y2)
    pendown()
    while y <= size:
        goto(x,y2)
        goto(x2,y)
        y = y + inc
        x = x + inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    y = size - (size * 2)
    x2 = size - (size * 2)
    x = 0
    y2 = size - (size * 2)
    penup()
    goto(x,y2)
    pendown()
    while y <= 0:
        goto(x,y2)
        goto(x2,y)
        y = y + inc
        x = x - inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    y = 0
    x2 = size
    x = size
    y2 = size - (size * 2)
    penup()
    goto(x,y2)
    pendown()
    while y >= size - (size * 2):
        goto(x,y2)
        goto(x2,y)
        y = y - inc
        x = x - inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    menu()

def four_point_star():
    global size
    global inc
    time.sleep(5)
    vary = 0
    varx = x
    while vary <= x:
        goto(varx,0)
        goto(0,vary)
        vary = vary + inc
        varx = varx - inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    vary = 0
    varx = x - (x * 2)
    goto(0,0)
    while vary <= x:
        goto(varx,0)
        goto(0,vary)
        vary = vary + inc
        varx = varx + inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    vary = 0
    varx = x - (x * 2)
    b = x - (x * 2)
    goto(0,0)
    while vary >= b:
        goto(varx,0)
        goto(0,vary)
        vary = vary - inc
        varx = varx + inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    vary = 0
    varx = x
    y = x - (2 * x)
    goto(0,0)
    while vary >= y:
        goto(varx,0)
        goto(0,vary)
        vary = vary - inc
        varx = varx - inc
        hexcolour = '#%02X%02X%02X' % (r(),r(),r())
        pencolor(hexcolour)
    menu()
    
def cyrcle_plus_four_point():
    four_point_star()
    cyrcle_square()
    menu()

def cyrcle_plus_eight_point():
    eight_point_star()
    cyrcle_square()
    menu()


def menu ():
    print("What curve patten would you like?(don't put in caps please)")
    print("four point star, cyrcle in a Square, eight point star, cyrcle plus eight point, cyrcle plus four point")
    answer = input("")
    if answer == "cyrcle in a square":
        print("Ok then")
        size_decider()
        cyrcle_square()
    if answer == "four point star":
        print("Ok then")
        size_decider()
        four_point_star()
    if answer == "eight point star":
        print("Ok then")
        size_decider()
        eight_point_star()
    if answer == "cyrcle plus eight point":
        print("Ok then")
        size_decider()
        cyrcle_plus_eight_point()
    if answer == "cyrcle plus four point":
        print("Ok then")
        size_decider()
        cyrcle_plus_four_point()
    else:
        print("I dont understand")
        menu()
menu()