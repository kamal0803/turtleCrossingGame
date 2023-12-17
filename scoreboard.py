from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-290, 250)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f"Level: {self.score}", align='left', font=FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()