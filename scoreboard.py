FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)

        self.goto(-280, 250)
        self.level = 1
        with open("./data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} | High Score: {self.high_score}", align= 'left', font= FONT)
    
    def increase_level(self):
        self.level +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        if self.level > self.high_score:
            with open("./data.txt", mode="w") as data:
                data.write(f"{self.level}")
        self.write(f"GAME OVER", align= 'center', font= FONT)
        