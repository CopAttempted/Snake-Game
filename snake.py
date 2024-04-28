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
            self.body[segment].goto(
                self.body[segment - 1].xcor(), self.body[segment - 1].ycor()
            )
        self.head.forward(25)

    def mv_up(self):
        self.head.setheading(90 if self.head.heading() != 270 else self.head.heading())

    def mv_down(self):
        self.head.setheading(270 if self.head.heading() != 90 else self.head.heading())

    def mv_right(self):
        self.head.setheading(0 if self.head.heading() != 180 else self.head.heading())

    def mv_left(self):
        self.head.setheading(180 if self.head.heading() != 0 else self.head.heading())

    def extend(self):
        block = Turtle()
        block.color("gray10")
        block.shape("square")
        block.shapesize(1.25)
        block.penup()
        block.goto(self.body[-1].position())
        self.body.append(block)

    def wall_collition(self):
        return (
            True
            if self.head.xcor() > 280
            or self.head.xcor() < -280
            or self.head.ycor() > 280
            or self.head.ycor() < -280
            else False
        )

    def tail_collition(self):
        for segment in self.body[1:]:
            return True if self.head.distance(segment) < 20 else False

