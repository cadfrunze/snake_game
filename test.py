from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.bgcolor('black')
screen.title(titlestring='The Snake game')
screen.tracer(0)
screen.listen()

# Pozitia de unde porneste sarpele
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segmente = []
for starting in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(starting)
    segmente.append(new_segment)


def la_stanga():
    segmente[0].left(90)


def la_dreapta():
    segmente[0].right(90)


def sus():
    segmente[0].setheading(90)


def jos():
    segmente[0].setheading(-90)

screen.onkey(key='a', fun=la_stanga)
screen.onkey(key='d', fun=la_dreapta)
screen.onkey(key='w', fun=sus)
screen.onkey(key='s', fun=jos)
jocul = True
while jocul:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segmente) - 1, 0, -1):
        new_x = segmente[seg_num - 1].xcor()
        new_y = segmente[seg_num - 1].ycor()
        segmente[seg_num].goto(x=new_x, y=new_y)
    segmente[0].forward(20)







screen.exitonclick()