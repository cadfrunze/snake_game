from turtle import Turtle
import random


class Food:
    def __init__(self):
        self.food = Turtle('circle')
        self.food.color('blue')
        self.food.penup()
        self.food.shapesize(0.8)
        self.x_cor = 0
        self.y_cor = 0

    def pozitia(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.food.goto(x=x, y=y)
        self.x_cor = self.food.xcor()
        self.y_cor = self.food.ycor()

    def reseteaza(self):
        self.food.clear()



