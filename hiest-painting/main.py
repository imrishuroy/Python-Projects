
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_colors.append(rgb_color)
#
# print(rgb_colors)

import turtle as turtle_module
from turtle import Screen
import random
turtle_module.colormode(255)


timmy = turtle_module.Turtle()
timmy.penup()
timmy.hideturtle()


color_list = [(131, 165, 206), (225, 151, 100), (32, 41, 59), (200, 134, 147), (235, 212, 87), (166, 56, 46), (39, 104, 153),
              (141, 184, 161), (153, 58, 65), (170, 29, 33), (217, 80, 69), (158, 32, 29),
              (15, 96, 71), (236, 165, 156), (50, 111, 90), (58, 50, 47), (50, 42, 46), (228, 164, 168),
              (34, 61, 56), (170, 188, 222), (190, 99, 108), (32, 59, 108), (103, 127, 163), (34, 151, 210),
              (175, 200, 188), (66, 66, 56)]


timmy.setheading(220)
timmy.forward(300)
timmy.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)




screen = Screen()
screen.exitonclick()