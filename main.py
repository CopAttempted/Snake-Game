from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.title("Snake Game")
screen.bgcolor("gray90")
screen.setup(width=600,height=600)

food = Food()
snake = Snake()
scoreboard = Scoreboard()
game_over = False

screen.listen()
screen.onkeypress(snake.mv_up, "Up")
screen.onkeypress(snake.mv_down, "Down")
screen.onkeypress(snake.mv_right, "Right")
screen.onkeypress(snake.mv_left, "Left")

while not game_over:
      screen.update()
      snake.move()
      sleep(0.25)

      if snake.tail_collition() or snake.wall_collition():
            game_over = True
            scoreboard.game_over()

      if snake.head.distance(food) <= 20:
            scoreboard.update_score()
            food.random_location()
            snake.extend()

screen.exitonclick()