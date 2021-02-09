from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS_PROBABILITY = 10
CARS_PROBABILITY_THRESHOLD = 2


class CarManager:
    def __init__(self):
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.probability_threshold = CARS_PROBABILITY_THRESHOLD
        self.generate_starting_cars()
        self.generate_starting_positions()

    def add_car(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        self.cars.append(new_car)

    def generate_new_car(self):
        choice = random.randint(0, CARS_PROBABILITY)
        if choice < self.probability_threshold:
            self.add_car()
            self.cars[-1].goto(300, random.randrange(-240, 240, 20))

    def generate_starting_cars(self):
        starting_cars_number = random.randint(15, 30)
        for _ in range(starting_cars_number):
            self.add_car()
        print(f"Generated {len(self.cars)} starting cars")

    def generate_starting_positions(self):
        for car in self.cars:
            car.goto(random.randint(-260, 260), random.randrange(-240, 240, 20))

    def move_cars(self):
        for car in self.cars:
            car.forward(self.cars_speed)

    def increase_speed(self):
        self.cars_speed += MOVE_INCREMENT

    def increase_probability_threshold(self):
        self.probability_threshold += 1

