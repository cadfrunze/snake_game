from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scor = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.modify_scor()

    def modify_scor(self):
        self.clear()
        super().write(arg=f"Scor: {self.scor}", move=False, align="center", font=('Arial', 14, 'normal'))






