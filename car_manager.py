from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):    
        random_chance = random.randint(1,6)
        if random_chance == 1:  # Generate a car every 6 frames
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-260,260) # Random y position
            new_car.goto(300, random_y)  
            self.all_cars.append(new_car) # Add the new car to the list
        
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move the car left
            
    def level_up(self):
        self.car_speed += MOVE_INCREMENT #Increase the cars speed