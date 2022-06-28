from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["green", "blue", "orange", "red", "purple", "brown", "yellow"]

#all_turtles = ["Casey", "Leonardo", "Mikey", "Raphael", "Donatello", "Splinter", "April"]
all_turtles = []
y_positions = [90, 60, 30, 0, -30, -60, -90]
for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.speed(0)
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've WON! The {winning_color} turtle is the winner!")
            else:
                print(f"You've LOST! The {winning_color} turtle was the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()

