from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(0.5, 0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh_position()

    def refresh_position(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
