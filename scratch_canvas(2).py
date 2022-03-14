import turtle
import random

def draw_circles(a,b):
    color = input("type the color of your circle")
    radius = int(input("type the radius"))
    turtle.penup()
    turtle.goto(random.randint(-150, 150) + 20, random.randint(150, -150) + 20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle
    turtle.end_fill()
    turtle.pencolor("black")
    turtle.goto(0,-200)
    turtle.stamp()
    
draw_circles(45,"red")