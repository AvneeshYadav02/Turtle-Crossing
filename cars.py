from turtle import Turtle
import random

CAR_COLORS = ['red', 'blue', 'green', 'orange', 'pink', 'violet']

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()
        self.speed = 5

    def create_car(self):
        self.color(CAR_COLORS[random.randint(0, 5)])
        self.setheading(180)
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(x=random.randint(-300, 300),y=random.randint(-200, 200))
    
    def move(self):
        self.forward(self.speed)
        if self.xcor()<-340:
            self.goto(x=350,y=random.randint(-200, 200))