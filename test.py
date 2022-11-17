from turtle import Turtle, Screen

t1 = Turtle()
screen = Screen()


miscare = 4
t1.write(arg=f"Scor: {miscare}", move=True, align="center")
t1.forward(miscare)

screen.exitonclick()
