from turtle import Turtle

MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
STARTING_POSITION = (0, -280)


class Player:

    def __init__(self):
        self.player_turtle = Turtle("turtle")
        self.player_score = 0

    def create_turtle(self):
        self.player_turtle.hideturtle()
        self.player_turtle.penup()
        self.start_again()
        self.player_turtle.left(90)
        self.player_turtle.showturtle()

    def go_up(self):
        self.player_turtle.forward(MOVE_DISTANCE)

    def start_again(self):
        self.player_turtle.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return self.player_turtle.ycor() > FINISH_LINE_Y

