COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import turtle as t
import random
t.colormode(255)
rgb_list = [(219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153), (245, 232, 236), (118, 82, 93), (179, 140, 150), (247, 251, 248), (41, 46, 65), (162, 104, 151), (126, 173, 114), (83, 96, 183), (67, 9, 27), (238, 241, 245), (81, 133, 107), (231, 188, 138), (52, 62, 79), (195, 90, 72), (116, 43, 58), (60, 41, 28), (92, 144, 117), (70, 67, 52), (182, 187, 207), (211, 181, 189), (102, 51, 38), (174, 199, 203), (181, 201, 180), (210, 184, 180), (41, 73, 82)]

class CarManager(t.Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("square")
        self.pu()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color((random.choice(rgb_list)))
        self.goto(300, random.randint(-250, 250))
        self.move_increment = 10


    def speed_increment(self):
        self.move_increment += MOVE_INCREMENT


