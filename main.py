import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from gameMaster import GameMaster

# screen = Screen()
# screen.setup(width=600, height=600)
#
#
# def set_up_screen():
#     screen.clear()
#     screen.tracer(0)
#     screen.bgcolor("black")
#     screen.listen()
#
#
# def set_up_control(player):
#     screen.onkeypress(player.move_up, "Up")
#     screen.onkey(new_game, "n")
#
#
# def new_game():
#     set_up_screen()
#     player = Player()
#     cars = CarManager()
#     set_up_control(player)
#     scoreboard = Scoreboard()
#
#     game_loop(player, cars, scoreboard)
#
#
# def game_loop(player, cars, scoreboard):
#     game_is_on = True
#     while game_is_on:
#         time.sleep(0.1)
#         screen.update()
#         cars.move_cars()
#
#         # Detect finish line
#         if player.detect_finish_line():
#             print("Finish achieved")
#             scoreboard.level_up()
#             cars.increase_speed()
#             cars.increase_probability_threshold()
#
#         # Detect collision with car
#         for car in cars.cars:
#
#             if abs(player.ycor() - car.ycor()) < 20 and player.distance(car) < 36:
#                 print(f"Collision with distance {player.distance(car)}")
#                 print(
#                     f"Car x: {car.xcor()}, Player x: {int(player.xcor())}, Car y: {car.ycor()}, "
#                     f"Player y: {player.ycor()}, ")
#                 scoreboard.game_over()
#                 game_is_on = False
#
#         cars.generate_new_car()


def game_loop():
    while True:
        game = GameMaster()
        game.new_game()
        game.screen.exitonclick()

# while True:
#     game = GameMaster()
#     game.new_game()
#     game.screen.exitonclick()
game_loop()


# set_up_screen()
# new_game()

