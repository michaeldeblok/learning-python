from turtle import Turtle, Screen, color, colormode
from random import randint

tim = Turtle()
tim.shape("turtle")
tim.color("tomato")

# # triangle
# for _ in range(3):
#     tim.forward(100)
#     tim.right(120)
#
# # square
# tim.color("light steel blue")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# # pentagon
# tim.color("medium spring green")
# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)
#
# # hexagon
# tim.color("moccasin")
# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)
#
# # heptagon
# tim.color("medium violet red")
# for _ in range(7):
#     tim.forward(100)
#     tim.right(51.428571428571428571428571428571)
#
# # octagon
# tim.color("red")
# for _ in range(8):
#     tim.forward(100)
#     tim.right(45)
#
# # nonagon
# tim.color("green")
# for _ in range(9):
#     tim.forward(100)
#     tim.right(40)
#
# # decagon
# tim.color("purple")
# for _ in range(10):
#     tim.forward(100)
#     tim.right(36)

colormode(255)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.width(10)
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
