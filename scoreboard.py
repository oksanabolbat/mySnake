from turtle import Turtle

FONT_ALIGNMENT = "center"
FONT_STYLE = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#fff")
        self.penup()
        self.goto(-20, 270)
        self.hideturtle()
        self.points = 0
        self.display_score()
        # self.write(arg=f"Score: {self.points}", move=True, align="center", font=("Courier", 16, "normal"))

    def display_score(self):
        self.write(arg=f"Score: {self.points}", align=FONT_ALIGNMENT, font=FONT_STYLE)

    def add_point(self):
        self.points += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=FONT_ALIGNMENT, font=FONT_STYLE)
