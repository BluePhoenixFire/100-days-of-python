from turtle import Turtle, Screen

import colorgram
from random import choice


def color_extractor(image_path: str = "image.jpg", number_of_colors: int = 30, white_filter: int = 245) -> list:
    rgb_colors: list[tuple[int, int, int]] = []
    colors = colorgram.extract(image_path, number_of_colors)
    for color in colors:
        if color.rgb.r < white_filter and color.rgb.g < white_filter and color.rgb.b < white_filter:
            rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return rgb_colors


#TODO func hist painter
# accepts, colorlist, rows, columns, spacing, circle size
# move turtle bottom left
# iterate rows by columns dropping circles
# random.choice - colors

def circle_placer(turt: Turtle, color_list: list[tuple[int,int,int]], circle_size: int = 20, spacing: int = 50) -> None:
    turt.pendown()
    turt.color(choice(color_list))
    turt.dot(circle_size)
    turt.penup()



def hirst_painter(turt: Turtle,
                  colorlist: list[tuple[int,int,int]],
                  x_pos,
                  y_pos,
                  rows: int = 10,
                  columns: int = 10,
                  spacing: int = 50,
                  circle_size: int = 20 ) -> None:
    temp_count: int = 0
    for _ in range(rows):
        watch_1 = temp_count * spacing
        y_pos_2 = y_pos + watch_1
        turt.setpos(x_pos, y_pos + temp_count * spacing )
        temp_count += 1
        for _ in range(columns):
            circle_placer(turt, colorlist, circle_size, spacing)
            turt.forward(spacing)



def main():
    # initial setup
    color_list = color_extractor()
    my_screen: Screen = Screen()
    my_screen.colormode(255)
    timmy: Turtle = Turtle()
    timmy.speed("fastest")

    x_pos = (-my_screen.window_width()/2) + (my_screen.window_width()/20)
    y_pos = (-my_screen.window_height()/2) + (my_screen.window_height()/20)
    timmy.penup()
    timmy.setpos(x_pos,y_pos)

    hirst_painter(timmy,color_list, x_pos, y_pos)

    my_screen.exitonclick()


if __name__ == "__main__":
    main()
