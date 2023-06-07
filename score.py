from turtle import Turtle
from tkinter import Tk

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
        self.update_score()

    def update_score(self):
        self.write(arg=f"Scor: {self.scor}", move=MOVE, align=ARANJARE, font=FONT)

    def modify_scor(self):
        self.clear()
        self.scor += 1
        self.update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Te-ai lovit de zid! Game over!", move=MOVE, align=ARANJARE, font=FONT)

    def game_over_muscat(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Te-ai muscat de coada! Game over!", move=MOVE, align=ARANJARE, font=FONT)
