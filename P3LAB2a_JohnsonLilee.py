# This program will have a turtle draw two shapes: a square and a triangle.
# Mr. Teter, CTI-110, P3LAB2a
# Lilee Johnson
# 19 Oct. 2021
#--------------------------------------------------------------------------
import turtle
turtle.pensize(4)           
turtle.pencolor("purple")
turtle.shape("turtle")
#square
for i in (1,2,3,4):
    turtle.forward(90)
    turtle.right(90)   
#triangle
turtle.forward(200)
for j in (1,2,3):
    turtle.left(125)
    turtle.forward(90)
    turtle.left(110)
