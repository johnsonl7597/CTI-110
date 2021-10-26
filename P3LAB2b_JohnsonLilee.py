# This program will have a turtle draw two Initials, mine are "LJ".
# Mr. Teter, CTI-110, P3LAB2b
# Lilee Johnson
# 21 Oct. 2021
#--------------------------------------------------------------------------
import turtle
t = turtle.Turtle()
t.pensize(10)           
t.pencolor("red")
t.shape("turtle")
#-----L-----
for i in range(1):
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.penup()  
#-----J-----
for j in range(1):
    t.forward(50)
    t.pendown()
    t.forward(100)
    
    t.penup()
    t.right(180)
    t.forward(100)
    t.pendown()
    t.right(90)
    t.forward(90)

    t.penup()
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(90)
    t.pendown()
    t.left(180)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(180)
    t.forward(200)
    

