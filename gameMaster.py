import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


class GameMaster:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.set_up_screen()
        self.scoreboard = Scoreboard()
        self.cars = CarManager()
        self.player = Player()
        self.set_up_control(self.player)
        self.game_loop(self.player, self.cars, self.scoreboard)

    def set_up_screen(self):
        self.screen.clear()
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.screen.listen()

    def set_up_control(self, player):
        self.screen.onkeypress(player.move_up, "Up")
        self.screen.onkey(self.new_game, "n")

    def new_game(self):
        self.__init__()
        self.set_up_screen()
        self.set_up_control(self.player)
        self.game_loop(self.player, self.cars, self.scoreboard)

    def game_loop(self, player, cars, scoreboard):
        game_is_on = True
        while game_is_on:
            time.sleep(0.1)
            self.screen.update()
            cars.move_cars()

            # Detect finish line
            if player.detect_finish_line():
                print("Finish achieved")
                scoreboard.level_up()
                cars.increase_speed()
                cars.increase_probability_threshold()

            # Detect collision with car
            for car in cars.cars:

                if abs(player.ycor() - car.ycor()) < 20 and player.distance(car) < 36:
                    print(f"Collision with distance {player.distance(car)}")
                    print(
                        f"Car x: {car.xcor()}, Player x: {int(player.xcor())}, Car y: {car.ycor()}, "
                        f"Player y: {player.ycor()}, ")
                    scoreboard.game_over()
                    game_is_on = False

            cars.generate_new_car()

