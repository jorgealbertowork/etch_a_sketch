import turtle

TIM = turtle.Turtle()
SCREEN = turtle.Screen()


def move_forwards():
    TIM.fd(10)


def move_backwards():
    TIM.bk(10)


def turn_left():
    TIM.lt(10)


def turn_right():
    TIM.rt(10)


def clear_screen():
    TIM.penup()
    TIM.clear()
    TIM.home()
    TIM.pendown()

SCREEN.listen()
SCREEN.onkeypress(key="w", fun=move_forwards)
SCREEN.onkeypress(key="s", fun=move_backwards)
SCREEN.onkeypress(key="a", fun=turn_left)
SCREEN.onkeypress(key="d", fun=turn_right)
SCREEN.onkeypress(key="c", fun=clear_screen)
SCREEN.exitonclick()
