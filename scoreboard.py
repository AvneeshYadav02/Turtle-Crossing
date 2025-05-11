from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Arial', 15, 'bold'

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.update()

    def update(self):
        self.penup()
        self.hideturtle()
        self.goto(x=-250, y=270)
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)
        
    def increase(self):
        self.level += 1
        self.clear()
        self.update()
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align='center', font=('Arial', 40, 'bold'))