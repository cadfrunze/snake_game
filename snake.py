from turtle import Turtle

# Creearea sarpelui
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Sablon sarpe"""

    def __init__(self):
        self.segmente = []
        self.create_snake()
        self.head = self.segmente[0]

    # Locul de unde porneste

    def create_snake(self):
        for seg in STARTING_POSITION:
            new_element = Turtle('square')
            new_element.penup()
            new_element.color('white')
            new_element.goto(seg)
            self.segmente.append(new_element)

    # Miscarea in fata, Atentie la capul sarpelui

    def move(self):
        for miscare in range(len(self.segmente) - 1, 0, -1):
            new_x = self.segmente[miscare - 1].xcor()
            new_y = self.segmente[miscare - 1].ycor()
            self.segmente[miscare].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    # Directiile

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
