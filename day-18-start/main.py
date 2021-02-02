import random
import turtle as t
from turtle import Screen

timmy = t.Turtle()
t.colormode(255)

# timmy.width(5)
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# colors = ["cyan", "chartreuse", "orange red", "dark slate blue",
#           "sandy brown", "yellow", "cadet blue", "blanched almond", "deep pink", "dodger blue"]

# counter = 0
# for a in range(100):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.circle(0, counter + 5)
#     timmy.circle(100)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)


# directions = [0, 90, 180, 270]
#
# for a in range(200):
#     timmy.color(random_color())
#     timmy.setheading(random.choice(directions))
#     timmy.forward(40)






# draw 10 shaped
# def shape_maker(side):
#     angle = 360 / side
#     for _ in range(side):
#         timmy.right(angle)
#         timmy.forward(100)
#
#
# for shape_side in range(3, 10):
#     timmy.color(random.choice(colors))
#     shape_maker(shape_side)














screen = Screen()
screen.exitonclick()

# timmy.shape("turtle")
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# timmy.color("black")
# timmy.forward(20)
# timmy.color("white")
# timmy.forward(20)
# timmy.color("black")


# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
#
