from turtle import Screen
import time
from snake import Snake
from food import Food
from score import AfisareScor

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.bgcolor('black')
screen.title(titlestring='The Snake game')
screen.tracer(0)
sarpele = Snake()
mancarea = Food()
afisare_scor = AfisareScor()
screen.listen()
screen.onkey(key='Up', fun=sarpele.move_up)
screen.onkey(key='Down', fun=sarpele.move_down)
screen.onkey(key='Left', fun=sarpele.move_left)
screen.onkey(key='Right', fun=sarpele.move_right)

mancarea.pozitia()

jocul = True
while jocul:
    screen.update()
    time.sleep(0.1)
    sarpele.move()
    adevarat_x = sarpele.x_cor - mancarea.x_cor
    adevarat_y = mancarea.y_cor - sarpele.y_cor
    print(f"adevarat_x: {adevarat_x}")
    print(f"adevarat_y: {adevarat_y}")
    print(f"scorul: {afisare_scor.scor}")
    if (adevarat_x <= 0.8 and adevarat_x >= -0.8) and (adevarat_y <= 0.8 and adevarat_y >= -0.8):
        afisare_scor.scor += 1
        mancarea.pozitia()









screen.exitonclick()
