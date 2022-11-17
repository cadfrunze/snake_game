from turtle import Turtle

ARANJARE = "center"
FONT = ('Arial', 14, 'normal')
MOVE = False

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scor = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.write(arg=f"Scor: {self.scor}", move=MOVE, align=ARANJARE, font=FONT)

    def modify_scor(self):
        self.clear()
        self.scor += 1
        super().write(arg=f"Scor: {self.scor}", move=MOVE, align=ARANJARE, font=FONT)






