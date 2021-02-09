from turtle import Turtle
FONT = ("Courier", 18, "bold")
COLOR = "white"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.goto(x=-270, y=260)
        self.show_level()

    def show_level(self):
        self.write(f"Level = {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        self.goto(0, -40)
        self.write("Press 'n' to start new game", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.show_level()
