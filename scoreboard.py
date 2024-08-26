from turtle import Turtle

FONT_ALIGNMENT = "center"
FONT_STYLE = ("Courier", 16, "normal")


def get_max_score():
    with open("score.txt") as score_file:
        score_contents = score_file.read()
        if "max_score:" in score_contents:
            return int(score_contents.split(":")[1])
    return 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#fff")
        self.penup()
        self.hideturtle()
        self.points = 0
        self.max_score = get_max_score()
        self.display_score()
        # self.write(arg=f"Score: {self.points}", move=True, align="center", font=("Courier", 16, "normal"))

    def display_score(self):
        self.clear()
        self.goto(-20, 270)
        self.write(arg=f"Max score: {self.max_score}. Score: {self.points}", align=FONT_ALIGNMENT, font=FONT_STYLE)

    def write_max_score(self):
        if self.max_score < self.points:
            with open("score.txt", mode="w") as score_file:
                score_file.write(f"max_score:{self.points}")

    def reset_scoreboard(self):
        self.points = 0
        self.max_score = get_max_score()
        self.display_score()

    def add_point(self):
        self.points += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=FONT_ALIGNMENT, font=FONT_STYLE)
        self.write_max_score()
        self.reset_scoreboard()
