from turtle import Turtle

class Snake(Turtle):

      def __init__(self):
            self.body = []
            self.head = Turtle()
            self.head.color("gray10")
            self.head.shapesize(1.25)
            self.head.shape("square")
            self.head.penup()
            self.body.append(self.head)
            self.extend()
            self.extend()

      def move(self):
            for segment in range(len(self.body) - 1, 0, -1):
                  x_axis = self.body[segment - 1].xcor()
                  y_axis = self.body[segment - 1].ycor()
                  self.body[segment].goto(x_axis, y_axis)
            self.head.forward(25)

      def mv_up(self):
            if self.head.heading() != 270:
                  self.head.setheading(90)

      def mv_down(self):
            if self.head.heading() != 90:
                  self.head.setheading(270)

      def mv_right(self):
            if self.head.heading() != 180:
                  self.head.setheading(0)

      def mv_left(self):
            if self.head.heading() != 0:
                  self.head.setheading(180)

      def extend(self):
            block = Turtle()
            block.color("gray10")
            block.shape("square")
            block.shapesize(1.25)
            block.penup()
            x_axis, y_axis = self.body[-1].position()
            block.goto(x_axis, y_axis)
            self.body.append(block)

      def wall_collition(self):
            if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
                  return True

      def tail_collition(self):
            for segment in self.body[1:]:
                  if self.head.distance(segment) < 20:
                        return True