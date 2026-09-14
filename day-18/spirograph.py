from turtle import Turtle, Screen
from random import randint, choice

def get_random_colour() -> tuple[int, int, int]:
    return randint(0,255),randint(0,255),randint(0,255)


def draw_shape(turtle: Turtle) -> None:
    timmy = turtle
    for x in range(3, 13):
        timmy.pencolor(get_random_colour())
        for _ in range(x):
            timmy.forward(50)
            timmy.rt(360/x)

def random_walk(timmy: Turtle, steps: int = 10, step_length: int = 10) -> None:
    directions: list [int] = [0, 90, 180, 270]
    for _ in range(steps):
        timmy.pencolor(get_random_colour())
        timmy.forward(step_length)
        timmy.setheading(choice(directions))

def random_walk_degrees(timmy: Turtle, steps: int = 10, step_length: int = 10) -> None:
    for _ in range(steps):
        timmy.pencolor(get_random_colour())
        timmy.forward(step_length)
        timmy.setheading(randint(0,359))

def spirograph(timmy: Turtle, radius: int = 100, no_of_circles: int = 36) -> None:
    for _ in range(no_of_circles):
        timmy.pencolor(get_random_colour())
        timmy.circle(radius)
        timmy.setheading(timmy.heading() + (360/no_of_circles))

def main() -> None:
    #initial setup
    my_screen: Screen = Screen()
    my_screen.colormode(255)
    timmy: Turtle = Turtle()
    timmy.speed("fastest")
    timmy.pensize(2)

    #adjust start location
    timmy.penup()
    timmy.setposition(0,0)
    timmy.pendown()

    spirograph(timmy,100,30)

    my_screen.exitonclick()

if __name__ == "__main__":
    main()
