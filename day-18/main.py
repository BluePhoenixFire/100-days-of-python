import random
from asyncio import __main__
from turtle import Turtle, Screen
from random import randint, choice

def get_random_colour() -> tuple[int, int, int]:
    return randint(1,255),randint(1,255),randint(1,255)


def draw_shape(turtle: Turtle) -> None:
    timmy = turtle
    for x in range(3, 13):
        timmy.pencolor(get_random_colour())
        for _ in range(x):
            timmy.forward(50)
            timmy.rt(360/x)

def random_walk(turtle: Turtle, steps: int = 10, step_length: int = 10) -> None:
    timmy: Turtle = turtle
    walks: int = steps
    walk_length: int = step_length
    for _ in range(walks):
        timmy.pencolor(get_random_colour())
        timmy.forward(walk_length)
        if randint(0,1) == 0:
            timmy.rt(random.choice([90,180,270,0]))
        else:
            timmy.lt(random.choice([90, 180, 270, 0]))
    pass

def main() -> None:
    #initial setup
    random.seed()
    my_screen: Screen = Screen()
    my_screen.colormode(255)
    timmy: Turtle = Turtle()
    timmy.speed("fastest")

    #adjust start location
    timmy.penup()
    timmy.setposition(-100,200)
    timmy.pendown()

    random_walk(timmy,500,10)

    my_screen.exitonclick()

if __name__ == "__main__":
    main()
