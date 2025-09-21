FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)

        self.goto(-280, 250)
        self.points = 0
        self.score()
        self.hideturtle()
    
    def score(self):
        self.clear()
        self.write(f"Score: {self.points}", align= 'left', font= FONT)
        self.points += 1
    pass