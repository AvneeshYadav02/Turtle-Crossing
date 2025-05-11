from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.shape('turtle')
        self.setheading(90)
        self.color('black')
        self.penup()
        self.goto(x=0, y=-280)

    #---------------------------------------------------------------
    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)
    #---------------------------------------------------------------