from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.restart()
        
    def move(self):
        self.fd(MOVE_DISTANCE)
        
    def success(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def restart(self):
        self.goto(STARTING_POSITION)
        
