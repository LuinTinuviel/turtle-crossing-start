import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from gameMaster import GameMaster

def game_loop():
    while True:
        game = GameMaster()
        game.new_game()
        game.screen.exitonclick()

game_loop()


