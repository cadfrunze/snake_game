from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.bgcolor('black')
screen.title(titlestring='The Snake game')
screen.tracer(0)
snake_food = Food()
sarpele = Snake()
scorul = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=sarpele.move_up)
screen.onkey(key='Down', fun=sarpele.move_down)
screen.onkey(key='Left', fun=sarpele.move_left)
screen.onkey(key='Right', fun=sarpele.move_right)

jocul = True
while jocul:
    screen.update()
    time.sleep(0.1)
    sarpele.move()
    # Intalnirea cu mancarea!
    if sarpele.head.distance(snake_food) < 15:
        scorul.scor += 1
        scorul.modify_scor()
        snake_food.refresh()
screen.exitonclick()
