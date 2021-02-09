from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.set_up_player()

    def set_up_player(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def detect_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.set_up_player()
            return True



