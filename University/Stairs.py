from turtle import *

penup()
goto(-290,0)
pendown()
for i in range(1, 9):
    for j in range(1, 4):
        forward(30)
        left(90)
        forward(30)
        right(90)
    penup()
    right(90)
    forward(90)
    left(90)
    pendown()
    
