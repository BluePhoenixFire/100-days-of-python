from turtle import Turtle, Screen
from random import randint

my_screen: Screen = Screen()
my_screen.colormode(255)
timmy: Turtle = Turtle()


def change_color():
    # Perform your periodic action
    timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
    timmy.forward(20)
    timmy.right(30)

    # Schedule the next call in 500 milliseconds (0.5 seconds)
    my_screen.ontimer(change_color, 500)


# Start the periodic function at once
change_color()

# Keep the window open and process events
my_screen.exitonclick()