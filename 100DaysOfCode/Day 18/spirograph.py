from turtle import Turtle, Screen, color, colormode
from random import randint

tim = Turtle()
tim.shape("turtle")
tim.speed(0)
colormode(255)

for _ in range(90):
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    tim.circle(150)
    tim.left(4)


screen = Screen()
screen.exitonclick()

