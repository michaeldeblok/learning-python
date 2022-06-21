from turtle import Turtle, Screen
#
tim = Turtle()
tim.shape("turtle")
tim.color("tomato")
#
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
#
# tim.left(180)
#
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#

for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()
#
#
# import heroes
# print(heroes.gen())

