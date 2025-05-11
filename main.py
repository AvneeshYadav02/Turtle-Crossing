from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player=Player()
score = Score()

screen.listen()
screen.onkey(player.go_up, 'w')
screen.onkey(player.go_down, 's')

car_list = []
for x in range(15):
    car=Cars()
    car_list.append(car)

game_is_on = True
speed = 0.1

while game_is_on:
    screen.update()
    time.sleep(speed)

    for x in range(len(car_list)):
        current_car = car_list[x]
        current_car.move()

        #Detect collision with Car
        if current_car.distance(player.pos()) < 25:
            game_is_on=False
            score.game_over()
    
    if player.ycor() > 280:
        player.goto(x=0, y=-280)
        if speed >= 0.025:
            speed /= 2
        score.increase()

screen.exitonclick()