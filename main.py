from turtle import Screen, Turtle
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
    if (adevarat_x <= 12 and adevarat_x >= -12) and (adevarat_y <= 12 and adevarat_y >= -12):
        afisare_scor.scor += 1
        screen.tracer()
        new_element = Turtle('square')
        new_element.hideturtle()
        new_element.penup()
        new_element.color('white')
        sarpele.segmente.append(new_element)
        sarpele.segmente[-1].showturtle()
        screen.update()
        time.sleep(0.1)
        mancarea.pozitia()









screen.exitonclick()
