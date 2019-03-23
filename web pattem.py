from turtle import *
import time
import random
y = 0
b = 0
speed(0)
r = lambda: random.randint(0,255)
hexcolour = '#%02X%02X%02X' % (r(),r(),r())
print("how long do you what your web to be?")
x = int(input())
inc = x / 100 * 5
vary = 0
varx = x

time.sleep(5)
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