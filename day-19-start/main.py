from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(15)


def move_backwards():
    timmy.backward(15)


def counter_clockwise():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def clockwise():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def clear_drawing():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
