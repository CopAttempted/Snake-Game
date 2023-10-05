from turtle import Turtle

class Scoreboard(Turtle):

      def __init__(self):
            super().__init__()
            self.score = 0
            self.color("gray10")
            self.penup()
            self.hideturtle()
            self.goto(0,250)
            self.write_score()

      def update_score(self):
            self.score += 1 
            self.clear()
            self.write_score()

      def write_score(self):
            self.write(f"Your score is {self.score}", move=False, align="center", font=("courier", 20, "bold"))

      def game_over(self):
            self.goto(0, 0)
            self.write("Game Over.",move=False, align="center", font=("courier", 25, "bold"))

