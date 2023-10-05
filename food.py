from turtle import Turtle
from random import randrange

class Food(Turtle):
      
      def __init__(self):
            super().__init__()
            self.color("chartreuse4")
            self.shape("square")
            self.shapesize(0.75)
            self.penup()
            self.random_location()

      def random_location(self):
            x_axis = randrange(-275, 275, 25)
            y_axis = randrange(-275, 275, 25)
            self.goto(x_axis, y_axis)