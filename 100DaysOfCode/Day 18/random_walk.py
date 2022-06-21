from turtle import Turtle, Screen, color, colormode
from random import randint

tim = Turtle()
tim.shape("turtle")
tim.speed(0)
colormode(255)



def random_walk():
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    tim.width(15)
    tim.setheading(randint(0, 360))
    tim.forward(30)


for _ in range(200):
    random_walk()


screen = Screen()
screen.exitonclick()

