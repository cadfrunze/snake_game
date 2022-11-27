from turtle import Turtle

# Creearea sarpelui
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    """Sablon sarpe"""

    def __init__(self):
        super().__init__()
        self.segmente = []
        self.create_snake()
        self.head = self.segmente[0]

    # Locul de unde porneste
    def create_snake(self):
        for seg in STARTING_POSITION:
            self.add_segment(seg)

    def add_segment(self, seg):
        new_element = Turtle('square')
        new_element.penup()
        new_element.color('white')
        new_element.goto(seg)
        self.segmente.append(new_element)

    def extented_sarpele(self):
        # Adauga o piesa la sarpe
        self.add_segment(self.segmente[-1].position())

    # Miscarea in fata, Atentie la capul sarpelui
    def move(self):
        for miscare in range(len(self.segmente) - 1, 0, -1):
            new_x = self.segmente[miscare - 1].xcor()
            new_y = self.segmente[miscare - 1].ycor()
            self.segmente[miscare].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)
        self.collision()

    def collision(self,):
        for num_piesa in self.segmente[1:]:
            if self.head.distance(num_piesa) < 10:
                return False

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
