from turtle import Turtle, Screen

screen = Screen()

t1 = Turtle()
t1.penup()
screen.listen()


def sus():
    t1.setheading(90)


def jos():
    t1.setheading(270)


def stanga():
    t1.setheading(180)


def dreapta():
    t1.setheading(0)


screen.onkey(key='Up', fun=sus)
screen.onkey(key='Down', fun=jos)
screen.onkey(key='Left', fun=stanga)
screen.onkey(key='Right', fun=dreapta)

joc = True
while joc:
    t1.forward(1)


screen.exitonclick()


